from OntologyConversorAbstract import OntologyConversorAbstract
from Project import Project
from Specimen import Specimen


class OntologyConversorHCA(OntologyConversorAbstract):

    ####################################################
    # region Define super class abstract methods

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

    def format_concrete_specimen(self, raw_specimen, specimen_id):
        specimen = Specimen(specimen_id)

        specimen.part_of_collection = "HumanCellAtlas"
        specimen.part_of_repository = "HumanCellAtlas"

        # Cell Lines
        specimen = self.__format_HCD_cell_lines(specimen, raw_specimen)

        # Cell Suspensions
        specimen = self.__format_HCD_cell_suspensions(specimen, raw_specimen)

        # Donor Organism
        specimen = self.__format_HCD_donor_organism(specimen, raw_specimen)

        # Projects
        specimen = self.__format_HCD_projects(specimen, raw_specimen)

        # File Type Summaries
        specimen = self.__format_HCD_file_type_summaries(specimen, raw_specimen)

        # Organoids
        specimen = self.__format_HCD_organoids(specimen, raw_specimen)

        # Protocols
        specimen = self.__format_HCD_protocols(specimen, raw_specimen)

        # Samples
        specimen = self.__format_HCD_samples(specimen, raw_specimen)

        # Specimens
        specimen = self.__format_HCD_specimens_SR(specimen, raw_specimen)

        self.specimen = specimen

    def format_concrete_project(self, raw_project, project_id):

        project = Project(project_id)

        project.part_of_collection = "HumanCellAtlas"
        project.part_of_repository = "HumanCellAtlas"

        # Cell Lines
        project = self.__format_HCD_cell_lines(project, raw_project)

        # Protocols
        project = self.__format_HCD_protocols(project, raw_project)

        # Projects
        project = self.__format_HCD_projects_PR(project, raw_project)

        # Samples
        project = self.__format_HCD_samples(project, raw_project)

        # Specimens
        project = self.__format_HCD_specimens_PR(project, raw_project)

        # Donor Organism
        project = self.__format_HCD_donor_organism_PR(project, raw_project)

        # Organoids
        project = self.__format_HCD_organoids(project, raw_project)

        # Cell Suspensions
        project = self.__format_HCD_cell_suspensions(project, raw_project)

        # File Type Summaries
        project = self.__format_HCD_file_type_summaries_PR(project, raw_project)

        project.project_id = raw_project["entryId"]

        self.project = project

    def parse_concrete(self, word):
        aux = list(word.title())

        for i in range(len(word)):
            if word[i].isupper():
                aux[i] = word[i]

        aux = ''.join(aux).replace(' ', '')

        return aux

    # endregion
    ####################################################

    ####################################################
    # region individual function auxiliar parts

    def __format_HCD_cell_lines(self, individual, individual_hca):
        if not individual_hca['cellLines']:
            return individual

        cell_line_type = individual_hca['cellLines'][0]['cellLineType']
        model_organ = individual_hca['cellLines'][0]['modelOrgan']

        individual.cell_line_type = self.parse_word(cell_line_type)
        individual.model_organ = self.parse_word(model_organ)

        return individual

    def __format_HCD_cell_suspensions(self, individual, individual_hca):
        if not individual_hca['cellSuspensions']:
            return individual

        selected_cell_type = []
        total_cells = 0

        for cellSuspension in individual_hca['cellSuspensions']:
            selected_cell_type += cellSuspension['selectedCellType']
            total_cells += cellSuspension['totalCells']

        if total_cells == 0:
            total_cells = -1

        individual.cell_type = self.parse_word(selected_cell_type)
        individual.total_cell_counts = total_cells

        return individual

    def __format_HCD_donor_organism(self, individual, individual_hca):
        if not individual_hca['donorOrganisms']:
            return individual

        biological_sex = individual_hca['donorOrganisms'][0]['biologicalSex']
        disease = individual_hca['donorOrganisms'][0]['disease']
        genus_species = individual_hca['donorOrganisms'][0]['genusSpecies']
        organism_age = individual_hca['donorOrganisms'][0]['organismAge'][0]
        organism_age_unit = individual_hca['donorOrganisms'][0]['organismAgeUnit']

        individual.biological_sex = biological_sex
        individual.disease = self.parse_word(disease)
        individual.specie = self.parse_word(genus_species)

        if organism_age is not None and '-' in organism_age:
            individual.min_age = int(organism_age.split('-')[0])
            individual.max_age = int(organism_age.split('-')[1])
        else:
            individual.min_age = int(float(organism_age)) if organism_age is not None else -1
            individual.max_age = int(float(organism_age)) if organism_age is not None else -1

        individual.age_unit = organism_age_unit

        return individual

    def __format_HCD_projects(self, individual, individual_hca):
        if not individual_hca['projects']:
            return individual

        laboratory = individual_hca['projects'][0]['laboratory']
        project_shortname = individual_hca['projects'][0]['projectShortname']
        project_title = individual_hca['projects'][0]['projectTitle']

        individual.laboratory = laboratory
        individual.project_short_name = project_shortname
        individual.project_title = project_title

        return individual

    def __format_HCD_organoids(self, individual, individual_hca):
        if not individual_hca['organoids']:
            return individual

        model_organ = individual_hca['organoids'][0]['modelOrgan']

        individual.model_organ = self.parse_word(model_organ)

        return individual

    def __format_HCD_protocols(self, individual, individual_hca):
        if not individual_hca['protocols']:
            return individual

        instrument_manufacturer_model = individual_hca['protocols'][0]['instrumentManufacturerModel']
        library_construction_approach = individual_hca['protocols'][0]['libraryConstructionApproach']
        paired_end = individual_hca['protocols'][0]['pairedEnd']
        workflow = individual_hca['protocols'][0]['workflow']

        individual.instrument = self.parse_word(instrument_manufacturer_model)
        individual.library = self.parse_word(library_construction_approach)
        individual.paired_end = paired_end
        individual.analysis_protocol = self.parse_word(workflow)

        return individual

    def __format_HCD_samples(self, individual, individual_hca):
        if not individual_hca['samples']:
            return individual

        sample_entity_type = individual_hca['samples'][0]['sampleEntityType']

        individual.sample_type = self.parse_word(sample_entity_type)

        try:
            preservation_method = individual_hca['samples'][0]['preservationMethod']

            individual.preservation = self.parse_word(preservation_method)

            return individual
        except:
            return individual

    def __format_HCD_file_type_summaries(self, individual, individual_hca):
        if not individual_hca['fileTypeSummaries']:
            return individual

        # It is possible that one individual has multiple files
        file_format = []
        # count = []
        total_size = []

        for i in range(len(individual_hca['fileTypeSummaries'])):
            ind_type = individual_hca['fileTypeSummaries'][i]['fileType']

            if ind_type != "matrix" and ind_type != "results":
                file_format.append(ind_type)

            # count.append(individual_hca['fileTypeSummaries'][i]['count'])
            total_size.append(individual_hca['fileTypeSummaries'][i]['totalSize'])

        individual.file_format = file_format
        individual.total_size_of_files = sum(total_size) / pow(2, 20)  # We save it in MB

        return individual

    # endregion
    ####################################################

    ####################################################
    #region specimen function auxiliar parts

    def __format_HCD_specimens_SR(self, specimen, specimen_hca):
        if not specimen_hca['specimens']:
            return specimen

        specimen = self.__format_HCD_specimens_PR(specimen, specimen_hca)

        sample_id = specimen_hca['specimens'][0]['id'][0]

        specimen.specimen_ID = sample_id

        return specimen
    #endregion
    ####################################################

    ####################################################
    #region project function auxiliar parts

    def __format_HCD_donor_organism_PR(self, project, project_hca):
        if not project_hca['donorOrganisms']:
            return project

        project = self.__format_HCD_donor_organism(project, project_hca)

        donor_count = project_hca['donorOrganisms'][0]['donorCount']

        project.donor_count = donor_count

        return project

    def __format_HCD_projects_PR(self, project, project_hca):
        if not project_hca['projects']:
            return project

        project_title = project_hca['projects'][0]['projectTitle']
        project_shortname = project_hca['projects'][0]['projectShortname']
        laboratory = project_hca['projects'][0]['laboratory']
        project_description = project_hca['projects'][0]['projectDescription']

        institutions = set()
        for contributor in project_hca['projects'][0]['contributors']:
            institutions.add(contributor["institution"])

        publication_titles = []
        publication_links = []
        for publication in project_hca['projects'][0]['publications']:
            publication_titles.append(publication['publicationTitle'])
            publication_links.append(publication['publicationUrl'])

        array_express = project_hca['projects'][0]['arrayExpressAccessions']
        geo_series = project_hca['projects'][0]['geoSeriesAccessions']
        insdc_project = project_hca['projects'][0]['insdcProjectAccessions']
        insdc_study = project_hca['projects'][0]['insdcStudyAccessions']
        supplementary_links = project_hca['projects'][0]['supplementaryLinks']

        project.project_title = project_title
        project.project_short_name = project_shortname
        project.laboratory = laboratory
        project.project_description = project_description
        project.institutions = list(institutions)
        project.publication_title = publication_titles
        project.publication_link = publication_links

        project.array_express_id = array_express
        project.geo_series_id = geo_series
        project.insdc_project_id = insdc_project
        project.insdc_study_id = insdc_study
        project.sumpplementary_link = supplementary_links

        return project

    def __format_HCD_file_type_summaries_PR(self, individual, individual_hca):
        if not individual_hca['fileTypeSummaries']:
            return individual

        # It is possible that one individual has multiple files
        file_type = ['metadata']
        file_format = ['tsv']
        count = []
        total_size = []

        for i in range(len(individual_hca['fileTypeSummaries'])):
            ind_type = individual_hca['fileTypeSummaries'][i]['fileType']

            if ind_type == 'matrix' and individual.project_title != "Systematic comparative " \
                                                                "analysis of single cell " \
                                                                "RNA-sequencing methods":
                file_type.append(ind_type)
            elif ind_type == 'results':
                file_type.append(ind_type)

            count.append(individual_hca['fileTypeSummaries'][i]['count'])
            total_size.append(individual_hca['fileTypeSummaries'][i]['totalSize'])

        if 'matrix' in file_type:
            file_format = file_format + ['loom', 'mtx', 'csv']

        individual.downloads_format = file_format
        individual.downloads_type = file_type
        individual.total_size_of_files = sum(total_size) / pow(2, 20)  # We save it in MB

        return individual

    def __format_HCD_specimens_PR(self, project, project_hca):
        if not project_hca['specimens']:
            return project

        organ = project_hca['specimens'][0]['organ']
        organ_part = project_hca['specimens'][0]['organPart']
        num_specimens = len(project_hca['specimens'][0]['id'])
        preservation_method = project_hca['specimens'][0]['preservationMethod']

        project.organism_part = self.parse_word(organ)
        project.biopsy_site = self.parse_word(organ_part)
        project.specimen_count = num_specimens
        project.preservation = self.parse_word(preservation_method)

        return project

    #endregion
    ####################################################

