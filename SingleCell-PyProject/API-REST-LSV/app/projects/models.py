# Modelos

from app.db import db, BaseModelMixin


class Project(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String)
    genes = db.relationship('Gene', backref='project', lazy=False, cascade='all, delete-orphan')

    def __init__(self, project_id, genes=[]):
        self.project_id = project_id
        self.genes = genes

    def __repr__(self):
        return f'Project({self.project_id})'

    def __str__(self):
        return f'{self.project_id}'


class Gene(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    cell_types = db.relationship('CellType', backref='gene', lazy=False, cascade='all, delete-orphan')
    project_id = db.Column(db.String, db.ForeignKey('project.project_id'), nullable=False)

    def __init__(self, name, cell_types=[]):
        self.name = name
        self.cell_types = cell_types

    def __repr__(self):
        return f'Gene({self.name})'

    def __str__(self):
        return f'{self.name}'


class CellType(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    percentil = db.Column(db.Float)
    gene_id = db.Column(db.Integer, db.ForeignKey('gene.id'), nullable=False)

    def __init__(self, name, percentil):
        self.name = name
        self.percentil = percentil

    def __repr__(self):
        return f'CellType({self.name})'

    def __str__(self):
        return f'{self.name}'
