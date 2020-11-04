from OntologyConversorHCA import OntologyConversorHCA

SAMPLE_ID_PREFIX = "SAMPLE_ID_"
PROJECT_ID_PREFIX = "PROJECT_ID_"


class OntologyCreator:

    def __init__(self):
        self.hca_conversor = OntologyConversorHCA()
        self.sample_id_counter = 0
        self.project_id_counter = 0
        self.samples = []
        self.projects = []

        super().__init__()

    def create_hca_sample(self, raw_sample):
        sample_id = SAMPLE_ID_PREFIX + str(self.sample_id_counter)

        sample = self.hca_conversor.format_sample(raw_sample, sample_id)
        self.samples.append(sample)

        self.sample_id_counter = self.sample_id_counter + 1

        return sample.get_dict()

    def create_hca_project(self, raw_project):
        project_id = SAMPLE_ID_PREFIX + str(self.project_id_counter)

        project = self.hca_conversor.format_project(raw_project, project_id)
        self.projects.append(project)

        self.project_id_counter = self.project_id_counter + 1

        return project
