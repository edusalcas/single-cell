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
      - users
    parameters:
      - in: body
        name: disease
        description: A disease on which a project has worked
      - in: body
        name: cell_type
        description: Cell type studied in a project
      - in: body
        name: sex
        description: Sex of the specimen studied on a project

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

    return projects
