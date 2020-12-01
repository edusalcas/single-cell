

class Individual:

    def __init__(self, ID):
        self.ID = ID

        self.analysis_protocol = None
        self.biopsy_site = None
        self.cell_line_type = None
        self.disease = None
        self.instrument = None
        self.kingdom = None
        self.library = None
        self.model_organ = None
        self.organism_part = None
        self.preservation = None
        self.sample_type = None
        self.cell_type = None
        self.specie = None

        self.age_unit = None
        self.biological_sex = None
        self.laboratory = None
        self.max_age = -1
        self.min_age = -1
        self.phenotype = None
        self.project_short_name = None
        self.project_title = None
        self.total_cell_counts = -1
        self.total_size_of_files = -1.0
        self.paired_end = None
        self.part_of_collection = None
        self.part_of_repository = None

        super().__init__()

    def get_dict(self):
        individual_dict = {
            "ID": self.ID,
            "ObjectProperties": {
                "SPR.hasAnalysisProtocol": self.analysis_protocol,
                "SPR.hasBiopsySite": self.biopsy_site,
                "SPR.hasCellLineType": self.cell_line_type,
                "SPR.hasDiseaseStatus": self.disease,
                "SPR.hasInstrument": self.instrument,
                "SPR.hasKingdom": self.kingdom,
                "SPR.hasLibrary": self.library,
                "SPR.hasModel": self.model_organ,
                "SPR.hasOrganismPart": self.organism_part,
                "SPR.hasPreservation": self.preservation,
                "SPR.hasSampleType": self.sample_type,
                "SPR.hasSelectedCellType": self.cell_type,
                "SPR.hasSpecie": self.specie,
            },
            "DataProperties": {
                "SPR.hasAgeUnit": self.age_unit,
                "SPR.hasBiologicalSex": self.biological_sex,
                "SPR.hasMaxAge": self.max_age,
                "SPR.hasMinAge": self.min_age,
                "SPR.hasPhenotype": self.phenotype,
                "SPR.hasTotalCellCount": self.total_cell_counts,
                "SPR.hasTotalSizeOfFilesInMB": self.total_size_of_files,
                "SPR.isPairedEnd": self.paired_end,
            },
            "AnnotationProperties": {
                "SPR.hasLaboratory": self.laboratory,
                "SPR.hasProjectShortName": self.project_short_name,
                "SPR.hasProjectTitle": self.project_title,
                "SPR.isPartOfCollection": self.part_of_collection,
                "SPR.isPartOfRepository": self.part_of_repository
            }
        }

        return individual_dict

    ####################################################
    #region Properties

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID):
        self.__ID = ID

    @property
    def analysis_protocol(self):
        return self.__analysis_protocol

    @analysis_protocol.setter
    def analysis_protocol(self, analysis_protocol):
        self.__analysis_protocol = analysis_protocol

    @property
    def cell_line_type(self):
        return self.__cell_line_type

    @cell_line_type.setter
    def cell_line_type(self, cell_line_type):
        self.__cell_line_type = cell_line_type

    @property
    def disease(self):
        return self.__disease

    @disease.setter
    def disease(self, disease):
        self.__disease = disease

    @property
    def instrument(self):
        return self.__instrument

    @instrument.setter
    def instrument(self, instrument):
        self.__instrument = instrument

    @property
    def library(self):
        return self.__library

    @library.setter
    def library(self, library):
        self.__library = library

    @property
    def model_organ(self):
        return self.__model_organ

    @model_organ.setter
    def model_organ(self, model_organ):
        self.__model_organ = model_organ

    @property
    def object_of_study(self):
        return self.__object_of_study

    @object_of_study.setter
    def object_of_study(self, object_of_study):
        self.__object_of_study = object_of_study

    @property
    def preservation(self):
        return self.__preservation

    @preservation.setter
    def preservation(self, preservation):
        self.__preservation = preservation

    @property
    def sample_type(self):
        return self.__sample_type

    @sample_type.setter
    def sample_type(self, sample_type):
        self.__sample_type = sample_type

    @property
    def cell_type(self):
        return self.__cell_type

    @cell_type.setter
    def cell_type(self, cell_type):
        self.__cell_type = cell_type

    @property
    def age_unit(self):
        return self.__age_unit

    @age_unit.setter
    def age_unit(self, age_unit):
        self.__age_unit = age_unit

    @property
    def downloads_format(self):
        return self.__downloads_format

    @downloads_format.setter
    def downloads_format(self, downloads_format):
        self.__downloads_format = downloads_format

    @property
    def downloads_type(self):
        return self.__downloads_type

    @downloads_type.setter
    def downloads_type(self, downloads_type):
        self.__downloads_type = downloads_type

    @property
    def biological_sex(self):
        return self.__biological_sex

    @biological_sex.setter
    def biological_sex(self, biological_sex):
        self.__biological_sex = biological_sex

    @property
    def laboratory(self):
        return self.__laboratory

    @laboratory.setter
    def laboratory(self, laboratory):
        self.__laboratory = laboratory

    @property
    def max_age(self):
        return self.__max_age

    @max_age.setter
    def max_age(self, max_age):
        self.__max_age = max_age

    @property
    def min_age(self):
        return self.__min_age

    @min_age.setter
    def min_age(self, min_age):
        self.__min_age = min_age

    @property
    def project_short_name(self):
        return self.__project_short_name

    @project_short_name.setter
    def project_short_name(self, project_short_name):
        self.__project_short_name = project_short_name

    @property
    def project_title(self):
        return self.__project_title

    @project_title.setter
    def project_title(self, project_title):
        self.__project_title = project_title

    @property
    def total_cell_counts(self):
        return self.__total_cell_counts

    @total_cell_counts.setter
    def total_cell_counts(self, total_cell_counts):
        self.__total_cell_counts = total_cell_counts

    @property
    def total_size_of_files(self):
        return self.__total_size_of_files

    @total_size_of_files.setter
    def total_size_of_files(self, total_size_of_files):
        self.__total_size_of_files = total_size_of_files

    @property
    def paired_end(self):
        return self.__paired_end

    @paired_end.setter
    def paired_end(self, paired_end):
        self.__paired_end = paired_end

    @property
    def part_of_collection(self):
        return self.__part_of_collection

    @part_of_collection.setter
    def part_of_collection(self, part_of_collection):
        self.__part_of_collection = part_of_collection

    @property
    def part_of_repository(self):
        return self.__part_of_repository

    @part_of_repository.setter
    def part_of_repository(self, part_of_repository):
        self.__part_of_repository = part_of_repository

    #endregion
    ####################################################
