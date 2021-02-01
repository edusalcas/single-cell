import requests
import json
import re
import time
import pandas as pd

from lxml import html
from IPython.display import clear_output


def get_info_from_html(experiment_ID):
    seed_url = "https://www.ebi.ac.uk/gxa/sc/experiments/" + experiment_ID + "/experiment-design"

    # Get the project samples information
    answer = requests.get(seed_url, headers=headers)

    # If couldn't get the information save the error
    if answer.status_code != requests.codes.ok:
        accessing_error.append(answer)
        clear_output(wait=True)
        return None

    # Parse response so we get the sample information
    parser = html.fromstring(answer.text)
    script_text = parser.xpath(".//div[@id='content']//script[3]/text()")
    match = re.search(r'content: (?P<value>{.*})', script_text[0])
    value = match.group('value')

    return json.loads(value)


def get_all_SCEA_projects():
    seed_url = "https://www.ebi.ac.uk/gxa/sc/json/experiments"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }

    answer = requests.get(seed_url, headers=headers)

    avoid_collections = ["Human Cell Atlas"]
    accessing_error = []
    n_experiments = len(answer.json()["experiments"])

    for n, experiment in enumerate(answer.json()['experiments']):
        experiment_ID = experiment['experimentAccession']

        # Print loop information
        print("Getting project \"" + experiment_ID + "\"")
        print("Number of errors: " + str(len(accessing_error)))
        print(f"{n + 1}/{n_experiments}")

        # If the projects is in a repository we already have we skip it
        if [i for i in experiment["experimentProjects"] if i in avoid_collections]:
            clear_output(wait=True)
            continue

        # --------------------------------
        #region Project Info

        # Wait between request so we dont overcharge server
        time.sleep(2.0)
        # Get the project samples information
        seed_url = "https://www.ebi.ac.uk/gxa/sc/experiments/" + experiment_ID + "/results/tsne"
        answer = requests.get(seed_url, headers=headers)

        # If couldn't get the information save the error
        if answer.status_code != requests.codes.ok:
            accessing_error.append(answer)
            clear_output(wait=True)
            continue

        # Parse response so we get the useful information
        parser = html.fromstring(answer.text)
        publication_link = parser.xpath(".//a[@class='pubmed-id']/@href")
        publication_title = parser.xpath(".//a[@class='pubmed-id']/text()")

        experiment['publication_link'] = publication_link
        experiment['publication_title'] = publication_title
        experiment['repository_link'] = seed_url
        experiment['supplementary_link'] = []
        #endregion
        # --------------------------------

        # --------------------------------
        #region Supplementary information

        # Get supplementary information
        seed_url = "https://www.ebi.ac.uk/gxa/sc/json/experiments/" + experiment_ID + "/resources/SUPPLEMENTARY_INFORMATION"
        ## Wait between request so we dont overcharge server
        time.sleep(2.0)

        answer = requests.get(seed_url, headers=headers)

        # If couldn't get the information save the error
        if answer.status_code != requests.codes.ok:
            accessing_error.append(answer)
            clear_output(wait=True)
            continue

        answer_json = answer.json()
        project['ENA_ID'] = None
        project['ArrayExpress_ID'] = None

        # For each repository information, save the id and the url of the project
        for group in answer.json():
            if group['type'] == 'icon-ena':  # If ENA repository
                ena_id_re = re.search('([SE]RP\d+)', group['description'])

                if not ena_id_re:
                    continue

                ena_id = ena_id_re.group(1)

                project['ENA_ID'] = ena_id
                project['supplementary_link'].append(group['url'])

            elif group['type'] == 'icon-ae':  # If Array Expression repository
                ae_id_re = re.search('(E-MTAB-\d+)', group['description'])

                if not ae_id_re:
                    continue

            ae_id = ae_id_re.group(1)

            project['ArrayExpress_ID'] = ae_id
            project['supplementary_link'].append(group['url'])

        else:
            continue
        #endregion
        # --------------------------------

        # --------------------------------
        #region Download information

        time.sleep(2.0)

        exp_info = get_info_from_html(experiment_ID)

        experiment['downloads'] = exp_info['tabs'][3]['props']['data']
        #endregion
        # --------------------------------

        # --------------------------------
        #region Experiment design

        exp_info_headers = exp_info['tabs'][1]['props']['table']['headers']
        column_names = exp_info_headers[0]['values'] + \
                       exp_info_headers[1]['values'] + \
                       exp_info_headers[2]['values']

        # Read tsv with experiment design data
        df = pd.read_csv(
            "https://www.ebi.ac.uk/gxa/sc/experiment/" + experiment_ID + "/download?fileType=experiment-design&accessKey=",
            sep="\t")

        # Delete Ontology terms columns
        cols = [c for c in df.columns if 'ontology term' not in c.lower()]
        df = df[cols]

        # Rename columns
        df.columns = column_names
        df = df.loc[:, ~df.columns.duplicated()]  # Drop duplicated columns

        # Remove assay column from df
        assay = df.Assay
        df = df.drop('Assay', axis=1)

        # Remove duplicated columns
        df = df.drop_duplicates()

        # experiment['cells'] = list(assay)

        for column in df:
            experiment[column] = list(df[column].unique())

        #endregion
        # --------------------------------
