from abc import ABC, abstractmethod
from Project import Project


class OntologyConversorAbstract (ABC):

    def __init__(self):
        self.sample = None
        self.project = None
        self.mapping_dict = self.init_map()

        super().__init__()

    def format_sample(self, raw_sample, sample_id):
        self.format_concrete_individual(raw_sample, sample_id)

        return self.sample

    def format_project(self, raw_project, project_id):
        self.format_concrete_project(raw_project, project_id)

        return self.project

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

    ####################################################
    #region Abstract methods
    @abstractmethod
    def init_map(self):
        pass

    @abstractmethod
    def format_concrete_individual(self, raw_sample, sample_id):
        pass

    @abstractmethod
    def format_concrete_project(self, raw_project, project_id):
        pass

    @abstractmethod
    def parse_concrete(self, word):
        pass

    #endregion
    ####################################################
