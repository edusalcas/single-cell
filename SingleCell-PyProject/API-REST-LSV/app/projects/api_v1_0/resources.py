from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import ProjectSchema, GeneSchema
from ..models import Project, CellType, Gene
from ...common.error_handling import ObjectNotFound

projects_v1_0_bp = Blueprint('projects_v1_0_bp', __name__)

project_schema = ProjectSchema()
gene_schema = GeneSchema()

api = Api(projects_v1_0_bp)


class ProjectListResource(Resource):
    def get(self):
        projects = Project.get_all()
        result = project_schema.dump(projects, many=True)

        return result

    def post(self):
        project_dict = request.json
        project = Project(project_id=project_dict['project_id'])
        for gene in project_dict['genes']:
            gene_ins = Gene(gene['name'])

            for cell_type in gene['cell_types']:
                gene_ins.cell_types.append(CellType(cell_type['name'], cell_type['percentile']))

            project.genes.append(gene_ins)

        project.save()
        resp = project_schema.dump(project)
        return resp, 201


class GeneListResource(Resource):
    def get(self, gene_name):
        gene = Gene.simple_filter(name=gene_name)
        if gene is None:
            raise ObjectNotFound('El gen no existe')
        resp = gene_schema.dump(gene, many=True)

        return resp


class ProjectResource(Resource):
    def get(self, project_id):
        project = Project.simple_filter(project_id=project_id)
        if project is None:
            raise ObjectNotFound('El proyecto no existe')
        resp = project_schema.dump(project, many=True)

        return resp


api.add_resource(ProjectListResource, '/api/v1.0/projects/', endpoint='project_list_resource')
api.add_resource(GeneListResource, '/api/v1.0/gene/<string:gene_name>', endpoint='gene_list_resource')

api.add_resource(ProjectResource, '/api/v1.0/projects/<string:project_id>', endpoint='project_resource')
