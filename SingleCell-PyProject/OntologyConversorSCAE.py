from OntologyConversorAbstract import OntologyConversorAbstract
from Project import Project


class OntologyConversorSCAE(OntologyConversorAbstract):

    def init_map(self):
        return {'PlasmodiumFalciparum3D7': 'PlasmodiumFalciparum'}

    def format_concrete_specimen(self, raw_specimen, specimen_id):
        pass

    def format_concrete_project(self, raw_project, project_id):

        project = Project(project_id)

        project.part_of_repository = "SingleCellExpresionAtlas"

        project.project_id = raw_project['experimentAccession']
        project.project_title = raw_project['experimentDescription']
        project.specie = self.parse_word(raw_project['species'])
        project.kingdom = self.parse_word(raw_project['kingdom'])
        project.load_date = raw_project['loadDate']
        project.update_date = raw_project['lastUpdate']
        project.total_cell_counts = raw_project['numberOfAssays']
        project.type = self.parse_word(raw_project['experimentType'])
        project.library = self.parse_word(raw_project['technologyType'])
        project.experimental_factor = self.parse_word(raw_project['experimentalFactors'])

        project.part_of_collection = self.parse_word(raw_project['experimentProjects'])
        project.sumpplementary_link = raw_project['supplementary_link']
        project.publication_title = raw_project['publication_title']
        project.publication_link = raw_project['publication_link']
        project.array_express_id = raw_project['ArrayExpress_ID']
        project.ena_id = raw_project['ENA_ID']


        self.project = project

    def parse_concrete(self, word):
        aux = list(word.title())

        for i in range(len(word)):
            if word[i].isupper():
                aux[i] = word[i]

        aux = ''.join(aux).replace(' ', '')

        return aux
