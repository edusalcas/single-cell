from OntologyConversorHCA import OntologyConversorHCA

ID_PREFIX = "ID_"


class OntologyCreator:

    def __init__(self):
        self.hca_conversor = OntologyConversorHCA()
        self.id_counter = 0
        self.individuals = []
        super().__init__()

    def create_hca_individual(self, raw_individual):
        individual_id = ID_PREFIX + str(self.id_counter)

        individual = self.hca_conversor.format_individual(raw_individual, individual_id)
        self.individuals.append(individual)

        self.id_counter = self.id_counter + 1

        return individual
