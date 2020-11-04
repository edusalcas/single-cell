from Individual import Individual


class Sample(Individual):

    def __init__(self, sample_id):
        self.specimen_ID = None

        super().__init__(sample_id)

    def get_dict(self):
        sample_dict = super().get_dict()

        sample_dict["DataProperties"]["SR.hasSpecimenID"] = self.specimen_ID

        return sample_dict

    ####################################################
    #region Sample properties

    @property
    def specimen_ID(self):
        return self.__specimen_ID

    @specimen_ID.setter
    def specimen_ID(self, specimen_ID):
        self.__specimen_ID = specimen_ID

    #endregion
    ####################################################
