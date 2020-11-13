from Individual import Individual


class Project(Individual):

    def __init__(self, project_id):
        self.project_description = None

        self.project_id = None
        self.array_express_id = None
        self.donor_count = None
        self.experimental_factor = None
        self.geo_series_id = None
        self.insdc_project_id = None
        self.insdc_study_id = None
        self.institution = []
        self.publication_title = None
        self.publication_link = None
        self.sumpplementary_link = None
        self.downloads_matrix_format = None
        self.downloads_metadata_format = None
        self.downloads_type = None

        super().__init__(project_id)

    def get_dict(self):
        project_dict = super().get_dict()

        project_dict["DataProperties"]["PR.hasDonorCount"] = self.donor_count
        project_dict["DataProperties"]["PR.hasExperimentalFactor"] = self.experimental_factor
        project_dict["DataProperties"]["PR.hasAvailableDownloadsMatrixFormat"] = self.downloads_matrix_format
        project_dict["DataProperties"]["PR.hasAvailableDownloadsMetadataFormat"] = self.downloads_metadata_format
        project_dict["DataProperties"]["PR.hasAvailableDownloadsType"] = self.downloads_type

        project_dict["AnnotationProperties"]["PR.hasArrayExpressID"] = self.array_express_id
        project_dict["AnnotationProperties"]["PR.hasDescription"] = self.project_description
        project_dict["AnnotationProperties"]["PR.hasGEOseriesID"] = self.geo_series_id
        project_dict["AnnotationProperties"]["PR.hasINSDCprojectID"] = self.insdc_project_id
        project_dict["AnnotationProperties"]["PR.hasINSDCstudyID"] = self.insdc_study_id
        project_dict["AnnotationProperties"]["PR.hasInstitution"] = self.institution
        project_dict["AnnotationProperties"]["PR.hasProjectID"] = self.project_id
        project_dict["AnnotationProperties"]["PR.hasPublicationLink"] = self.publication_link
        project_dict["AnnotationProperties"]["PR.hasPublicationTitle"] = self.publication_title
        project_dict["AnnotationProperties"]["PR.hasSumpplementaryLink"] = self.sumpplementary_link

        return project_dict

    ####################################################
    #region Project properties

    @property
    def array_express_id(self):
        return self.__array_express_id

    @array_express_id.setter
    def array_express_id(self, array_express_id):
        self.__array_express_id = array_express_id

    @property
    def donor_count(self):
        return self.__donor_count

    @donor_count.setter
    def donor_count(self, donor_count):
        self.__donor_count = donor_count

    @property
    def experimental_factor(self):
        return self.__experimental_factor

    @experimental_factor.setter
    def experimental_factor(self, experimental_factor):
        self.__experimental_factor = experimental_factor

    @property
    def geo_series_id(self):
        return self.__geo_series_id

    @geo_series_id.setter
    def geo_series_id(self, geo_series_id):
        self.__geo_series_id = geo_series_id

    @property
    def insdc_project_id(self):
        return self.__insdc_project_id

    @insdc_project_id.setter
    def insdc_project_id(self, insdc_project_id):
        self.__insdc_project_id = insdc_project_id

    @property
    def insdc_study_id(self):
        return self.__insdc_study_id

    @insdc_study_id.setter
    def insdc_study_id(self, insdc_study_id):
        self.__insdc_study_id = insdc_study_id

    @property
    def institution(self):
        return self.__institution

    @institution.setter
    def institution(self, institution):
        self.__institution = institution

    @property
    def publication(self):
        return self.__publication

    @publication.setter
    def publication(self, publication):
        self.__publication = publication

    @property
    def sumpplementary_link(self):
        return self.__sumpplementary_link

    @sumpplementary_link.setter
    def sumpplementary_link(self, sumpplementary_link):
        self.__sumpplementary_link = sumpplementary_link

    #endregion
    ####################################################
