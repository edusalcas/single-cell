from OntologyConversorAbstract import OntologyConversorAbstract
from Sample import Sample


class OntologyConversorHCA(OntologyConversorAbstract):

    ####################################################
    #region Define super class abstract methods

    def init_map(self):
        mapping_dict = {
            'Melanoma(Disease)': 'Melanoma',
            'Cataract(Disease)': 'Cataract',
            'UlcerativeColitis(Disease)': 'UlcerativeColitis',
            'Colitis(Disease)': 'UlcerativeColitis',
            'BenignProstaticHyperplasia(Disease)': 'BenignProstaticHyperplasia',
            'PericardialEffusion(Disease)': 'PericardialEffusion',
            'HiatusHernia(Disease)': 'HiatusHernia',
            'Hyperlipidemia(Disease)': 'Hyperlipidemia',
            'Non-AlcoholicFattyLiverDisease': 'NonAlcoholicFattyLiverDisease',
            'Hemolytic-UremicSyndrome': 'HemolyticUremicSyndrome',
            'Osteoarthritis,Hip': 'OsteoarthritisHip',
            'CAFs': 'Cancer-associatedFibroblasts(CAFs)',
            'IlluminaHiseq2500': 'IlluminaHiSeq2500',
            'Smart-Seq2': 'Smart-seq2',
            'Smart-Seq': 'Smart-seq',
            'Sci-RNA-Seq': 'Sci-RNA-seq',
            'MARS-Seq': 'MARS-seq',
            'CEL-Seq2': 'CEL-seq2',
            'CITE-Seq': 'CITE-seq',
            'DroNc-Seq': 'DroNc-seq',
            'Drop-Seq': 'Drop-seq',
            'Seq-Well': 'Seq-well',
            'TCell': 'Tcell',
            'CD8-Positive,Alpha-BetaTCell': 'CD8-positive_Alpha-betaTCell',
            'CD11B+CD11C+DC': 'CD11b+CD11c+DC',
            'CD11C+DC': 'CD11c+DC',
            'CD11B+Macrophages/Monocytes': 'CD11b+Macrophages/Monocytes',
            'CD34-Positive,CD38-NegativeHematopoieticStemCell': 'CD34-positive_CD38-negative_HematopoieticStemCell',
            'EffectorMemoryCD8-Positive,Alpha-BetaTCell,TerminallyDifferentiated': 'EffectorMemoryCD8-positive_Alpha-betaTCell_TerminallyDifferentiated',
            '10XV2Sequencing': '10Xv2Sequencing',
            '10XV3Sequencing': '10xv3Sequencing',
            "10X3'V1Sequencing": "10X3'v1Sequencing",
            "10X3'V2Sequencing": "10X3'v2Sequencing",
            "10X3'V3Sequencing": "10x3'v3Sequencing",
            "10X5'V2Sequencing": "10X5'v2Sequencing",
            'CDNALibraryConstruction': 'cDNALibraryConstruction',
            'BladderOrgan': 'Bladder',
            'MuscleOrgan': 'Muscle',
            'SkinOfBody': 'Skin',
            'Cryopreservation,Other': 'CryopreservationOther',
            'CryopreservationInLiquidNitrogen(DeadTissue)': 'CryopreservationInLiquidNitrogenDeadTissue',
            'Optimus_V1.3.1': 'Optimus_v1.3.1',
            'Optimus_V1.3.2': 'Optimus_v1.3.2',
            'Optimus_V1.3.3': 'Optimus_v1.3.3',
            'Optimus_V1.3.5': 'Optimus_v1.3.5',
            'Smartseq2_V2.3.0': 'Smartseq2_v2.3.0',
            'Smartseq2_V2.4.0': 'Smartseq2_v2.4.0',
            'StemCell-Derived': 'StemCell-derived',
        }

        return mapping_dict

    def format_concrete_individual(self, raw_sample, sample_id):
        sample = Sample(sample_id)

        sample.part_of_collection = "HumanCellAtlas"
        sample.part_of_repository = "HumanCellAtlas"

        # Cell Lines
        sample = self.__format_HCD_cell_lines(sample, raw_sample)

        # Cell Suspensions
        sample = self.__format_HCD_cell_suspensions(sample, raw_sample)

        # Donor Organism
        sample = self.__format_HCD_donor_organism(sample, raw_sample)

        # Projects
        sample = self.__format_HCD_projects(sample, raw_sample)

        # File Type Summaries
        sample = self.__format_HCD_file_type_summaries(sample, raw_sample)

        # Organoids
        sample = self.__format_HCD_organoids(sample, raw_sample)

        # Protocols
        sample = self.__format_HCD_protocols(sample, raw_sample)

        # Samples
        sample = self.__format_HCD_samples(sample, raw_sample)

        # Specimens
        sample = self.__format_HCD_specimens(sample, raw_sample)

        self.sample = sample

    def format_concrete_project(self, raw_project):
        project = self.project

        # TODO parsear las partes del proyecto

        self.project = project

    def parse_concrete(self, word):
        aux = list(word.title())

        for i in range(len(word)):
            if word[i].isupper():
                aux[i] = word[i]

        aux = ''.join(aux).replace(' ', '')

        return aux

    #endregion
    ####################################################

    ####################################################
    # region format_concrete_individual function auxiliar parts

    def __format_HCD_cell_lines(self, sample, sample_hca):
        if not sample_hca['cellLines']:
            return sample

        cell_line_type = sample_hca['cellLines'][0]['cellLineType']
        model_organ = sample_hca['cellLines'][0]['modelOrgan']

        sample.cell_line_type = self.parse_word(cell_line_type)
        sample.model_organ = self.parse_word(model_organ)

        return sample

    def __format_HCD_cell_suspensions(self, sample, sample_hca):
        if not sample_hca['cellSuspensions']:
            return sample

        organ = sample_hca['cellSuspensions'][0]['organ']
        organ_part = sample_hca['cellSuspensions'][0]['organPart']
        selected_cell_type = sample_hca['cellSuspensions'][0]['selectedCellType']
        total_cells = sample_hca['cellSuspensions'][0]['totalCells']

        sample.object_of_study = self.parse_word(organ_part) + self.parse_word(organ)

        sample.cell_type = self.parse_word(selected_cell_type)
        sample.total_cell_counts = total_cells

        return sample

    def __format_HCD_donor_organism(self, sample, sample_hca):
        if not sample_hca['donorOrganisms']:
            return sample

        biological_sex = sample_hca['donorOrganisms'][0]['biologicalSex']
        disease = sample_hca['donorOrganisms'][0]['disease']
        genus_species = sample_hca['donorOrganisms'][0]['genusSpecies']
        organism_age = sample_hca['donorOrganisms'][0]['organismAge'][0]
        organism_age_unit = sample_hca['donorOrganisms'][0]['organismAgeUnit']

        sample.biological_sex = biological_sex
        sample.disease = self.parse_word(disease)
        sample.specie = self.parse_word(genus_species)

        if organism_age is not None and '-' in organism_age:
            sample.min_age = int(organism_age.split('-')[0])
            sample.max_age = int(organism_age.split('-')[1])
        else:
            sample.min_age = int(float(organism_age)) if organism_age is not None else -1
            sample.max_age = int(float(organism_age)) if organism_age is not None else -1

        sample.age_unit = organism_age_unit

        return sample

    def __format_HCD_projects(self, sample, sample_hca):
        if not sample_hca['projects']:
            return sample

        laboratory = sample_hca['projects'][0]['laboratory']
        project_shortname = sample_hca['projects'][0]['projectShortname']
        project_title = sample_hca['projects'][0]['projectTitle']

        sample.laboratory = self.parse_word(laboratory)
        sample.project_short_name = project_shortname
        sample.project_title = project_title

        return sample

    def __format_HCD_file_type_summaries(self, sample, sample_hca):
        if not sample_hca['fileTypeSummaries']:
            return sample

        # It is possible that one individual has multiple files
        file_type = ['metadata']
        file_format = []
        count = []
        total_size = []

        for i in range(len(sample_hca['fileTypeSummaries'])):
            ind_type = sample_hca['fileTypeSummaries'][i]['fileType']

            if ind_type == 'matrix' and sample.project_title != "Systematic comparative " \
                                                                                           "analysis of single cell " \
                                                                                           "RNA-sequencing methods":
                file_type.append(ind_type)
            elif ind_type == 'results':
                file_type.append(ind_type)
            else:
                file_format.append(ind_type)

            count.append(sample_hca['fileTypeSummaries'][i]['count'])
            total_size.append(sample_hca['fileTypeSummaries'][i]['totalSize'])

        sample.downloads_format = file_format
        sample.downloads_type = file_type
        sample.total_size_of_files = sum(total_size) / pow(2, 20) # We save it in MB

        return sample

    def __format_HCD_organoids(self, sample, sample_hca):
        if not sample_hca['organoids']:
            return sample

        model_organ = sample_hca['organoids'][0]['modelOrgan']

        sample.model_organ = self.parse_word(model_organ)

        return sample

    def __format_HCD_protocols(self, sample, sample_hca):
        if not sample_hca['protocols']:
            return sample

        instrument_manufacturer_model = sample_hca['protocols'][0]['instrumentManufacturerModel']
        library_construction_approach = sample_hca['protocols'][0]['libraryConstructionApproach']
        paired_end = sample_hca['protocols'][0]['pairedEnd']
        workflow = sample_hca['protocols'][0]['workflow']

        sample.instrument = self.parse_word(instrument_manufacturer_model)
        sample.library = self.parse_word(library_construction_approach)
        sample.paired_end = paired_end
        sample.analysis_protocol = self.parse_word(workflow)

        return sample

    def __format_HCD_samples(self, sample, sample_hca):
        if not sample_hca['samples']:
            return sample

        sample_entity_type = sample_hca['samples'][0]['sampleEntityType']

        sample.sample_type = self.parse_word(sample_entity_type)

        try:
            preservation_method = sample_hca['samples'][0]['preservationMethod']

            sample.preservation = self.parse_word(preservation_method)

            return sample
        except:
            return sample

    def __format_HCD_specimens(self, sample, sample_hca):
        if not sample_hca['specimens']:
            return sample

        sample_id = sample_hca['specimens'][0]['id'][0]
        organ = sample_hca['specimens'][0]['organ']
        organ_part = sample_hca['specimens'][0]['organPart']
        preservation_method = sample_hca['specimens'][0]['preservationMethod']

        sample.specimen_ID = sample_id
        sample.object_of_study = self.parse_word(organ_part) + self.parse_word(organ)

        sample.preservation = self.parse_word(preservation_method)

        return sample

    # endregion
    ####################################################

    