from OntologyConversorAbstract import OntologyConversorAbstract


class OntologyConversorHCA (OntologyConversorAbstract):

    ####################################################
    # Define abstract methods
    ####################################################

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

    def format_concrete(self, raw_individual):
        individual = self.individual

        individual['DataProperties']['isPartOfCollection'] = "HumanCellAtlas"
        individual['DataProperties']['isPartOfRepository'] = "HumanCellAtlas"

        # Cell Lines
        individual = self.__format_HCD_cell_lines(individual, raw_individual)

        # Cell Suspensions
        individual = self.__format_HCD_cell_suspensions(individual, raw_individual)

        # Donor Organism
        individual = self.__format_HCD_donor_organism(individual, raw_individual)

        # Projects
        individual = self.__format_HCD_projects(individual, raw_individual)

        # File Type Summaries
        individual = self.__format_HCD_file_type_summaries(individual, raw_individual)

        # Organoids
        individual = self.__format_HCD_organoids(individual, raw_individual)

        # Protocols
        individual = self.__format_HCD_protocols(individual, raw_individual)

        # Samples
        individual = self.__format_HCD_samples(individual, raw_individual)

        # Specimens
        individual = self.__format_HCD_specimens(individual, raw_individual)

        self.individual = individual

    def parse_concrete(self, word):
        aux = list(word.title())

        for i in range(len(word)):
            if word[i].isupper():
                aux[i] = word[i]

        aux = ''.join(aux).replace(' ', '')

        return aux

    ####################################################
    # Main function auxiliar parts
    ####################################################

    def __format_HCD_cell_lines(self, individual, individual_hcd):
        if not individual_hcd['cellLines']:
            return individual

        cell_line_type = individual_hcd['cellLines'][0]['cellLineType']
        model_organ = individual_hcd['cellLines'][0]['modelOrgan']

        individual['ObjectProperties']['SR.hasCellLineType'] = self.parse_word(cell_line_type)
        individual['DataProperties']['hasModelOrgan'] = (model_organ is not None)

        return individual

    def __format_HCD_cell_suspensions(self, individual, individual_hcd):
        if not individual_hcd['cellSuspensions']:
            return individual

        organ = individual_hcd['cellSuspensions'][0]['organ']
        organ_part = individual_hcd['cellSuspensions'][0]['organPart']
        selected_cell_type = individual_hcd['cellSuspensions'][0]['selectedCellType']
        total_cells = individual_hcd['cellSuspensions'][0]['totalCells']

        individual['ObjectProperties']['SR.hasObjectOfStudy'] = self.parse_word(organ_part) if organ_part[
                                                                                                   0] is not None else self.parse_word(
            organ)
        individual['ObjectProperties']['SR.hasSelectedCellType'] = self.parse_word(selected_cell_type)

        individual['DataProperties']['hasTotalCellCounts'] = total_cells

        return individual

    def __format_HCD_donor_organism(self, individual, individual_hcd):
        if not individual_hcd['donorOrganisms']:
            return individual

        biological_sex = individual_hcd['donorOrganisms'][0]['biologicalSex']
        disease = individual_hcd['donorOrganisms'][0]['disease']
        donor_count = individual_hcd['donorOrganisms'][0]['donorCount']
        genus_species = individual_hcd['donorOrganisms'][0]['genusSpecies']
        organism_age = individual_hcd['donorOrganisms'][0]['organismAge'][0]
        organism_age_unit = individual_hcd['donorOrganisms'][0]['organismAgeUnit']

        individual['DataProperties']['hasBiologicalSex'] = biological_sex
        individual['ObjectProperties']['SR.hasDiseaseStatus'] = self.parse_word(disease)
        individual['ObjectProperties']['SR.hasGenusSpecie'] = self.parse_word(genus_species)

        if organism_age is not None and '-' in organism_age:
            individual['DataProperties']['hasMinAge'] = int(organism_age.split('-')[0])
            individual['DataProperties']['hasMaxAge'] = int(organism_age.split('-')[1])
        else:
            individual['DataProperties']['hasMinAge'] = int(float(organism_age)) if organism_age is not None else -1
            individual['DataProperties']['hasMaxAge'] = int(float(organism_age)) if organism_age is not None else -1

        individual['DataProperties']['hasAgeUnit'] = organism_age_unit
        individual['DataProperties']['hasTotalDonorCounts'] = donor_count

        return individual

    def __format_HCD_projects(self, individual, individual_hcd):
        if not individual_hcd['projects']:
            return individual

        laboratory = individual_hcd['projects'][0]['laboratory']
        project_shortname = individual_hcd['projects'][0]['projectShortname']
        project_title = individual_hcd['projects'][0]['projectTitle']

        individual['DataProperties']['hasLaboratory'] = self.parse_word(laboratory)
        individual['DataProperties']['hasProjectShortName'] = project_shortname
        individual['DataProperties']['hasProjectTitle'] = project_title

        return individual

    def __format_HCD_file_type_summaries(self, individual, individual_hcd):
        if not individual_hcd['fileTypeSummaries']:
            return individual

        # It is possible that one individual has multiple files
        file_type = ['metadata']
        file_format = []
        count = []
        total_size = []

        for i in range(len(individual_hcd['fileTypeSummaries'])):
            ind_type = individual_hcd['fileTypeSummaries'][i]['fileType']

            if ind_type == 'matrix' and individual['DataProperties']['hasProjectTitle'] != "Systematic comparative " \
                                                                                           "analysis of single cell " \
                                                                                           "RNA-sequencing methods":
                file_type.append(ind_type)
            elif ind_type == 'results':
                file_type.append(ind_type)
            else:
                file_format.append(ind_type)

            count.append(individual_hcd['fileTypeSummaries'][i]['count'])
            total_size.append(individual_hcd['fileTypeSummaries'][i]['totalSize'])

        individual['DataProperties']['hasAvailableDownloadsFormat'] = file_format
        individual['DataProperties']['hasAvailableDownloadsType'] = file_type
        individual['DataProperties']['hasTotalSizeOfFiles'] = sum(total_size) / pow(2, 20)

        return individual

    def __format_HCD_organoids(self, individual, individual_hcd):
        if not individual_hcd['organoids']:
            return individual

        model_organ = individual_hcd['organoids'][0]['modelOrgan']

        individual['ObjectProperties']['hasModelOrgan'] = (model_organ is not None)

        return individual

    def __format_HCD_protocols(self, individual, individual_hcd):
        if not individual_hcd['protocols']:
            return individual

        instrument_manufacturer_model = individual_hcd['protocols'][0]['instrumentManufacturerModel']
        library_construction_approach = individual_hcd['protocols'][0]['libraryConstructionApproach']
        paired_end = individual_hcd['protocols'][0]['pairedEnd']
        workflow = individual_hcd['protocols'][0]['workflow']

        individual['ObjectProperties']['SR.hasInstrument'] = self.parse_word(instrument_manufacturer_model)
        individual['ObjectProperties']['SR.hasLibrary'] = self.parse_word(library_construction_approach)
        individual['DataProperties']['isPairedEnd'] = paired_end
        individual['ObjectProperties']['SR.hasAnalysisProtocol'] = self.parse_word(workflow)

        return individual

    def __format_HCD_samples(self, individual, individual_hcd):
        if not individual_hcd['samples']:
            return individual

        sample_entity_type = individual_hcd['samples'][0]['sampleEntityType']

        individual['ObjectProperties']['SR.hasSampleType'] = self.parse_word(sample_entity_type)

        try:
            preservation_method = individual_hcd['samples'][0]['preservationMethod']

            individual['ObjectProperties']['SR.hasPreservation'] = self.parse_word(preservation_method)

            return individual
        except:
            return individual

    def __format_HCD_specimens(self, individual, individual_hcd):
        if not individual_hcd['specimens']:
            return individual

        individual_id = individual_hcd['specimens'][0]['id'][0]
        organ = individual_hcd['specimens'][0]['organ']
        organ_part = individual_hcd['specimens'][0]['organPart']
        preservation_method = individual_hcd['specimens'][0]['preservationMethod']

        individual['DataProperties']['hasId'] = individual_id
        individual['ObjectProperties']['SR.hasObjectOfStudy'] = self.parse_word(organ_part) if organ_part[
                                                                                                   0] is not None else self.parse_word(
            organ)
        individual['ObjectProperties']['SR.hasPreservation'] = self.parse_word(preservation_method)

        return individual
