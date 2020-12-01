from OntologyConversorHCA import OntologyConversorHCA
from OntologyConversorSCAE import OntologyConversorSCAE

SPECIMEN_ID_PREFIX = "SPECIMEN_ID_"
PROJECT_ID_PREFIX = "PROJECT_ID_"


def format_id_number(number_id):
    number_str = str(number_id)

    while len(number_str) < 3:
        number_str = '0' + number_str

    return number_str


class OntologyCreator:

    def __init__(self):
        self.hca_conversor = OntologyConversorHCA()
        self.scae_conversor = OntologyConversorSCAE()
        self.specimen_id_counter = 0
        self.project_id_counter = 0
        self.specimens = []
        self.projects = []

        super().__init__()

    def create_hca_specimen(self, raw_specimen):
        specimen_id = SPECIMEN_ID_PREFIX + format_id_number(self.specimen_id_counter)

        specimens = self.hca_conversor.format_specimen(raw_specimen, specimen_id)
        self.specimens.append(specimens)

        self.specimen_id_counter = self.specimen_id_counter + 1

        return specimens.get_dict()

    def create_hca_project(self, raw_project):
        project_id = PROJECT_ID_PREFIX + format_id_number(self.project_id_counter)

        project = self.hca_conversor.format_project(raw_project, project_id)
        self.projects.append(project)

        self.project_id_counter = self.project_id_counter + 1

        return project.get_dict()

    def create_scae_project(self, raw_project):
        project_id = PROJECT_ID_PREFIX + format_id_number(self.project_id_counter)

        project = self.scae_conversor.format_project(raw_project, project_id)
        self.projects.append(project)

        self.project_id_counter = self.project_id_counter + 1

        return project.get_dict()
