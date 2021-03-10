import requests
import pandas as pd
import json

server_name = 'http://194.4.103.244:3030'
service_name = 'ds'
request_url = server_name + '/' + service_name
URI_prefix = 'http://www.semanticweb.org/alicia/ontologies/2020/8/singleCellRepositories#'


def conn_alive():
    ans = requests.get(request_url, data={'query': '{}'})

    return ans.status_code == 200


def __fuseki_to_dict(response):
    rows = []
    headers = response.json()["head"]["vars"]
    results = response.json()["results"]['bindings']

    for result in results:
        result_dict = {}
        for header in headers:
            if header not in result:
                result_dict[header] = None
            else:
                value = result[header]['value']

                if URI_prefix in value:
                    value = value.split('#')[-1]
                result_dict[header] = value

        rows.append(result_dict)

    df = pd.DataFrame(rows)

    projects = []
    for project_ID, data in df.groupby('project_ID'):
        project = {
            'project_ID': project_ID,
        }

        for column in [x for x in data if x != 'project_ID']:
            column_data = data[column].unique().tolist()
            if len(column_data) == 1:
                column_data = column_data[0]

            if column_data is not None:
                project[column] = column_data

        projects.append(project)

    return projects


def __fuseki_to_list(response):
    items = []
    header = response.json()["head"]["vars"][0]
    results = response.json()["results"]['bindings']
    for result in results:
        item = result[header]['value']
        if URI_prefix in item:
            item = item.split('#')[-1]
        items.append(item)

    return items


def get_projects(params={}):
    where_content = "?project rdf:type a:Project . ?project a:PR.hasProjectID ?project_ID ."

    for key, value in params.items():
        if key == 'disease':
            where_content += " ?project a:SPR.hasDisease a:" + value + " ."
        elif key == 'cell_type':
            where_content += " ?project a:SPR.hasCellType a:" + value + " ."
        elif key == 'organism_part':
            where_content += " ?project a:SPR.hasOrganismPart \"" + value + "\" ."
        elif key == 'sex':
            where_content += " ?project a:SPR.hasSex \"" + value + "\" ."
        else:
            return {'msg': 'Param key not valid'}

    where_content += '''
        OPTIONAL { ?project a:SPR.hasProjectTitle ?projectTitle . }
        OPTIONAL { ?project a:PR.hasDescription ?description . }
        OPTIONAL { ?project a:SPR.hasAnalysisProtocol ?analysisProtocol . }
        OPTIONAL { ?project a:SPR.hasLibrary ?library . }
        OPTIONAL { ?project a:SPR.hasCellType ?cellType . }
        OPTIONAL { ?project a:SPR.hasSex ?sex . }
        OPTIONAL { ?project a:SPR.hasDisease ?disease . }
        OPTIONAL { ?project a:SPR.hasMinAge ?minAge . }
        OPTIONAL { ?project a:SPR.hasMinAge ?maxAge . }
        OPTIONAL { ?project a:SPR.hasAgeUnit ?ageUnit . }
        OPTIONAL { ?project a:SPR.hasOrganismPart ?organismPart . }
        OPTIONAL { ?project a:SPR.hasBiopsySite ?biopsySite . }
        OPTIONAL { ?project a:SPR.hasLaboratory ?laboratory . }
        OPTIONAL { ?project a:PR.hasInstitution ?institution . }
        OPTIONAL { ?project a:SPR.isPartOfRepository ?repository . }
        OPTIONAL { ?project a:SPR.isPartOfCollection ?collection . }
        OPTIONAL { ?project a:PR.hasDonorCount ?donorCount . }
        OPTIONAL { ?project a:PR.hasSpecimenCount ?specimenCount . }
    '''

    query = '''
        PREFIX a: <http://www.semanticweb.org/alicia/ontologies/2020/8/singleCellRepositories#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT 
            ?project_ID
            ?projectTitle
            ?description
            ?analysisProtocol
            ?cellType
            ?sex
            ?minAge
            ?maxAge
            ?ageUnit
            ?disease
            ?organismPart
            ?biopsySite
            ?laboratory
            ?institution
            ?repository
            ?collection
            ?donorCount
            ?specimenCount
        WHERE { ''' + where_content + '}'

    print(query)

    response = requests.post(request_url, data={'query': query})

    projects = __fuseki_to_dict(response)

    print(projects)

    return projects


def get_project_metadata(metadata_param):
    where_content = "?project rdf:type a:Project ."

    if metadata_param == 'disease':
        where_content += " ?project a:SPR.hasDisease ?x ."
    elif metadata_param == 'cell_type':
        where_content += " ?project a:SPR.hasCellType ?x ."
    elif metadata_param == 'sex':
        where_content += " ?project a:SPR.hasSex ?x ."
    elif metadata_param == 'library':
        where_content += " ?project a:SPR.hasLibrary ?x ."
    elif metadata_param == 'organism_part':
        where_content += " ?project a:SPR.hasOrganismPart ?x ."
    elif metadata_param == 'specie':
        where_content += " ?project a:SPR.hasSpecie ?x ."
    elif metadata_param == 'analysis_protocol':
        where_content += " ?project a:SPR.hasAnalysisProtocol ?x ."
    elif metadata_param == 'instrument':
        where_content += " ?project a:SPR.hasInstrument ?x ."
    else:
        return {'msg': 'Param key not valid'}

    query = '''
            PREFIX a: <http://www.semanticweb.org/alicia/ontologies/2020/8/singleCellRepositories#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT DISTINCT
                ?x
            WHERE { ''' + where_content + '}'

    print(query)

    response = requests.post(request_url, data={'query': query})

    metadata_list = __fuseki_to_list(response)

    return metadata_list


def get_project_downloads(project_ID):
    where_content = f"?project rdf:type a:Project . ?project a:PR.hasProjectID \"{project_ID}\" ."

    where_content += '''
            OPTIONAL { ?project a:PR.hasProjectID ?project_ID . }
            OPTIONAL { ?project a:SPR.hasClusteringLink ?clusteringLink . }
            OPTIONAL { ?project a:SPR.hasExperimentDesignLink ?experimentDesignLink . }
            OPTIONAL { ?project a:SPR.hasExperimentMetadataLink ?experimentMetadataLink . }
            OPTIONAL { ?project a:SPR.hasFilteredTPMLink ?filteredTPMLink . }
            OPTIONAL { ?project a:SPR.hasMarkerGenesLink ?markerGenesLink . }
            OPTIONAL { ?project a:SPR.hasMatrixLink ?matrixLink . }
            OPTIONAL { ?project a:SPR.hasNormalisedCountsLink ?normalisedCountsLink . }
            OPTIONAL { ?project a:SPR.hasRawCountsLink ?rawCountsLink . }
            OPTIONAL { ?project a:SPR.hasResultsLink ?resultsLink . }
        '''

    query = '''
            PREFIX a: <http://www.semanticweb.org/alicia/ontologies/2020/8/singleCellRepositories#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT
                ?project_ID
                ?clusteringLink
                ?experimentDesignLink
                ?experimentMetadataLink
                ?filteredTPMLink
                ?markerGenesLink
                ?matrixLink
                ?normalisedCountsLink
                ?rawCountsLink
                ?resultsLink
            WHERE { ''' + where_content + '}'

    print(query)

    response = requests.post(request_url, data={'query': query})
    downloads = __fuseki_to_dict(response)

    return downloads
