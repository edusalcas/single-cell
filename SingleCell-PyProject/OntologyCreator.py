from OntologyConversorHCA import OntologyConversorHCA

SAMPLE_ID_PREFIX = "SAMPLE_"
PROJECT_ID_PREFIX = "PROJECT_"


class OntologyCreator:

    def __init__(self):
        self.hca_conversor = OntologyConversorHCA()
        self.sample_id_counter = 0
        self.project_id_counter = 0
        self.individuals = []
        self.projects = []
        super().__init__()

    def create_hca_individual(self, raw_individual):
        individual_id = SAMPLE_ID_PREFIX + str(self.sample_id_counter)

        individual = self.hca_conversor.format_individual(raw_individual, individual_id)
        self.individuals.append(individual)

        self.sample_id_counter = self.sample_id_counter + 1

        return individual

    def create_hca_project(self, raw_project):
        project_id = SAMPLE_ID_PREFIX + str(self.project_id_counter)

        project = self.hca_conversor.format_project(raw_project, project_id)
        self.projects.append(project)

        self.project_id_counter = self.project_id_counter + 1

        return project
