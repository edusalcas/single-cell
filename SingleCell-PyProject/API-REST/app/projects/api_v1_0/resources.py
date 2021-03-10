import ast

from flask import request, Blueprint, jsonify
from flask_restful import Api, Resource

from ...db_conn import fuseki_con

from ...common.error_handling import ObjectNotFound

projects_v1_0_bp = Blueprint('projects_v1_0_bp', __name__)

api = Api(projects_v1_0_bp)


@projects_v1_0_bp.route("/project", methods=['GET'])
def get_projects():
    """
    Get a list of projects using some parameters
    ---
    tags:
      - projects
    parameters:
      - in: body
        name: disease
        description: A disease on which a project has worked
        type: string
      - in: body
        name: cell_type
        description: Cell type studied in a project
        type: string
      - in: body
        name: sex
        description: Sex of the specimen studied on a project
        type: string

    responses:
      200:
        description: List of projects that meet selected parameters
    """
    if not fuseki_con.conn_alive():
        return jsonify({'Internal error': 'Internal server is dead'})

    params = {}

    disease = request.values.get('disease')
    if disease is not None:
        params['disease'] = disease

    cell_type = request.values.get('cell_type')
    if cell_type is not None:
        params['cell_type'] = cell_type

    sex = request.values.get('sex')
    if sex is not None:
        params['sex'] = sex

    projects = fuseki_con.get_projects(params)

    return jsonify(projects)


@projects_v1_0_bp.route("/project/metadata", methods=['GET'])
def get_project_metadata():
    """
        Get a list of possible values for a metadata parameter
        ---
        tags:
          - metadata
        parameters:
          - in: body
            name: param
            description: A metadata parameter ('disease', 'cell_type', 'organism_part' and 'sex' at the moment)
            required: true
            type: string

        responses:
          200:
            description: List of values for metadata parameter
    """
    if not fuseki_con.conn_alive():
        return jsonify({'Internal error': 'Internal server is dead'})

    metadata_param = request.values.get('param')

    if metadata_param is None:
        return jsonify({'msg': 'param needed'})

    metadata_list = fuseki_con.get_project_metadata(metadata_param)

    return jsonify(metadata_list)


@projects_v1_0_bp.route("/project/downloads", methods=['GET'])
def get_project_downloads():
    """
        Get download links for a given project
        ---
        tags:
          - downloads
        parameters:
          - in: body
            name: project_ID
            description: Project ID of a specific project
            required: true
            type: string

        responses:
          200:
            description: List of download links of the project
    """
    project_ID = request.values.get('project_ID')

    if project_ID is None:
        return jsonify({'msg': 'project_ID needed'})

    downloads = fuseki_con.get_project_downloads(project_ID)

    return jsonify(downloads)


@projects_v1_0_bp.route("/percentiles", methods=['GET'])
def get_percentile():
    '''
        Get percentiles of the projects given a filter
        ---
        tags:
          - percentiles
        parameters:
          - in: body
            name: filters
            description: filters of the percentiles
            required: true
            type: json
            schema:
                gen_names:

        responses:
          200:
            description: List of download links of the project
    '''

    filters = request.values.get('filters')
    filters = ast.literal_eval(filters)

    gen_names = []
    cell_types = []
    project_IDs = []

    print(filters)

    for key, value in filters.items():
        if key == 'gen_names':
            gen_names = value
        elif key == 'cell_types':
            cell_types = value
        elif key == 'project_IDs':
            project_IDs = value

    percentiles = fuseki_con.get_percentile(gen_names, cell_types, project_IDs)

    return jsonify(percentiles)