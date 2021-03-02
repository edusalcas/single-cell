import requests
import pandas as pd

server_name = 'http://194.4.103.244:3030'
service_name = 'ds'
request_url = server_name + '/' + service_name


def conn_alive():
    ans = requests.get(request_url, data={'query': '{}'})

    return ans.status_code == 200


def __fuseki_to_df(response):
    rows = []
    headers = response.json()["head"]["vars"]
    results = response.json()["results"]['bindings']

    for result in results:
        result_dict = {}
        for header in headers:
            result_dict[header] = result[header]['value']

        rows.append(result_dict)

    df = pd.DataFrame(rows)

    return df


def get_projects(params={}):
    where_content = "?project rdf:type a:Project . ?project a:PR.hasProjectID ?project_ID ."

    for key, value in params.items():
        if key == 'disease':
            where_content += " ?project a:SPR.hasDisease a:" + value + " ."
        if key == 'cell_type':
            where_content += " ?project a:SPR.hasCellType a:" + value + " ."
        if key == 'sex':
            where_content += " ?project a:SPR.hasSex \"" + value + "\" ."

    query = '''
        PREFIX a: <http://www.semanticweb.org/alicia/ontologies/2020/8/singleCellRepositories#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT 
            ?project_ID
        WHERE { ''' + where_content + '}'

    print(query)

    response = requests.post(request_url, data={'query': query})

    df = __fuseki_to_df(response)


    return df.to_json(orient="records")
