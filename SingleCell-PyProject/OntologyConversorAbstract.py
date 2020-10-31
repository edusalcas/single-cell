from abc import ABC, abstractmethod


def init_individual():
    individual = {
        "ID": None,
        "ObjectProperties": {
            "SR.belongsToSpecie": None,
            "SR.hasAnalysisProtocol": None,
            "SR.hasCellLineType": None,
            "SR.hasDiseaseStatus": None,
            "SR.hasInstrument": None,
            "SR.hasLibrary": None,
            "SR.hasModelOrgan": None,
            "SR.hasObjectOfStudy": [],
            "SR.hasPreservation": None,
            "SR.hasSampleType": None,
            "SR.hasSelectedCellType": None,
        },
        "DataProperties": {
            "hasAgeUnit": None,
            "hasAvailableDownloadsFormat": None,
            "hasAvailableDownloadsType":None,
            "hasBiologicalSex": None,
            "hasLaboratory": None,
            "hasMaxAge": -1,
            "hasMinAge": -1,
            "hasProjectShortName": None,
            "hasProjectTitle": None,
            "hasSampleID": None,
            "hasTotalCellCounts": -1,
            "hasTotalSizeOfFiles": -1,
            "isPairedEnd": False,
            "isPartOfCollection": None,
            "isPartOfRepository": None,
        }
    }

    return individual


class OntologyConversorAbstract (ABC):

    def __init__(self):
        self.individual = None
        self.mapping_dict = self.init_map()
        super().__init__()

    def format_individual(self, raw_individual, individual_id):
        self.individual = init_individual()
        self.format_concrete(raw_individual)

        self.individual["ID"] = individual_id

        return self.individual

    def parse_word(self, word):
        # If word is None, return None
        if word is None:
            return None

        # If text is a list, apply parse_word for each item
        if type(word) is list:
            return list(map(self.parse_word, word))

        # Parse word depending on the repository
        word_parsed = self.parse_concrete(word)

        # Map word if necessary
        try:
            word_mapped = self.mapping_dict[word_parsed]
            return word_mapped
        except KeyError:
            return word_parsed

    @abstractmethod
    def init_map(self):
        pass

    @abstractmethod
    def format_concrete(self, raw_individual):
        pass

    @abstractmethod
    def parse_concrete(self, word):
        pass
