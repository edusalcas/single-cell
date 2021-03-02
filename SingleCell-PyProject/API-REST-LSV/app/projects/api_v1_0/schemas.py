# Esquemas para serializar los modelos

from marshmallow import fields

from app.ext import ma


class ProjectSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    project_id = fields.String()
    genes = fields.Nested('GeneSchema', many=True)


class GeneSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    project_id = fields.String()
    cell_types = fields.Nested('CellTypeSchema', many=True)


class CellTypeSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    percentil = fields.Float()