from OntologyConversorAbstract import OntologyConversorAbstract
from Project import Project


def norm2control(disease):
    if type(disease) is list:
        return list(map(norm2control, disease))

    if disease == 'Normal':
        disease = "Control"

    return disease


class OntologyConversorSCAE(OntologyConversorAbstract):

    def init_map(self):
        mapping_dict = {
            # Specie
            'PlasmodiumFalciparum3D7': 'PlasmodiumFalciparum',
            # Downloads
            'ExperimentDesignFile(TSVFormat)': 'ExperimentDesign',
            'ExperimentMetadata(SDRFAndIDFFilesArchive)': 'ExperimentMetadata',
            'ClusteringFile(TSVFormat)': 'Clustering',
            'FilteredTPMsFiles(MatrixMarketArchive)': 'FilteredTPMs',
            'MarkerGeneFiles(TSVFilesArchive)': 'MarkerGenes',
            'NormalisedCountsFiles(MatrixMarketArchive)': 'NormalisedCounts',
            'RawCountsFiles(MatrixMarketArchive)': 'RawCounts',
            # Sex
            'male-to-female transsexual': 'trans',
            'not available': 'notAvailable',
            'mixed sex population': 'mixed',
            'not applicable': 'notApplicable',
            'mixed sex': 'mixed',
            # Organism Part
            'DorsalSkin': 'Skin',
            'ProstateGland': 'Prostate',
            'ZonaPellucida': 'PellucidZone',
            'brain without olfactory bulb': 'Brain',
            'primary visual area, layer…': 'PrimaryVisualArea',
            'CaudalGanglionicEminence': 'GanglionicEminence',
            'AnteriorNeuralTube': 'NeuralTube',
            'SplanchnicLayerOfLateralPlateMesoderm': 'Mesoderm',
            'SmoothMuscle,Peri-UrethralMesenchymeAndUrethralEpithelium': 'PeriUrethralMesenchyme',
            'VentralMedialGanglionicEminence': 'GanglionicEminence',
            'DorsalMedialGanglionicEminence': 'GanglionicEminence',
            'Embryonic/LarvalLymphGland': 'LymphNode',
            'PrimaryVisualArea,Layer1,Layer2/3AndLayer4': 'PrimaryVisualArea',
            'PrimaryVisualArea,Layer6A': 'PrimaryVisualArea',
            'PrimaryVisualCortex': 'PrimaryVisualArea',
            'PrimaryVisualArea,Layer5AndLayer6': 'PrimaryVisualArea',
            'PrimaryVisualArea,Layer1AndLayer2/3': 'PrimaryVisualArea',
            'PrimaryVisualArea,Layer2/3': 'PrimaryVisualArea',
            'PrimaryVisualArea,Layer4': 'PrimaryVisualArea',
            'PrimaryVisualArea,Layer6B': 'PrimaryVisualArea',
            'PrimaryVisualArea,Layer1': 'PrimaryVisualArea',
            'PrimaryVisualArea,Layer6': 'PrimaryVisualArea',
            'Cortical-LikeVentricle-Region1': 'CorticalLikeVentricle',
            'Cortical-LikeVentricle-Region2': 'CorticalLikeVentricle',
            'Cortical-LikeVentricle-Region3': 'CorticalLikeVentricle',
            'Cortical-LikeVentricle-Region4': 'CorticalLikeVentricle',
            'MetastasisToLymphNode': 'Metastasis',
            'BrainWithoutOlfactoryBulb': 'Brain',
            'NormalTissueAdjacentToTumour': 'NormalTissueAdjacentToTumor',
            'MixedCervicalAndThoracicVertebrae': ['CervicalVertebrae', 'ThoracicVertebrae'],
            'Fibroblasts': 'Fibroblast',
            'Embryonic/LarvalHemolymph': 'Hemolymph',
            'CardiacNon-MyocyteAndCardiomyocyte': ['CardiacNonMyocyte', 'Cardiomyocyte'],
            # Biopsy Site
            'Ascites': 'AsciticFluid',
            'LeftSupraclavicularLymphNode': 'LymphNode',
            'AlveolusOfLung': 'Alveolus',
            'PrimaryTumor': 'Tumor',
            'PeripheralRegionOfRetina': 'Retina',
            'ProximalSmallIntestine': 'SmallIntestine',
            'MiddleAirway': 'RespiratoryAirway',
            'TumourCore': 'Tumor',
            'RightEye': 'Eye',
            'AdjacentToTumor': 'Tumor',
            'LaminaPropriaOfSmallIntestine': 'LaminaPropiaOfSmallIntestine',
            # Disease
            'ChronicPhaseChronicMyeloidLeukemia': 'MyeloidLeukemia',
            'BronchioalveolarCarcinoma;Non-SmallCellLungCancer': 'BronchioalveolarCarcinoma',
            'MetastaticBreastCancer': 'BreastCancer',
            'ProstateCarcinoma': 'ProstateCancer',
            'BreastCarcinoma': 'BreastCancer',
            'PancreaticNeoplasm': 'PancreaticCancer',
            'LungAdenocarcinoma': 'LungCarcinoma',
            'BrainGlioblastoma': 'Glioblastoma',
            'HypocellularMyelodysplasticSyndrome': 'MyelodysplasticSyndrome',
            'Crohn\'SDisease': 'CrohnsDisease',
            'HIVInfection': 'HIV',
            'OvarianSerousAdenocarcinoma': 'OvarianCarcinoma',
            'TypeIDiabetesMellitus': 'Type1DiabetesMellitus',
            'TypeIIDiabetesMellitus': 'Type2DiabetesMellitus',
            'Parkinson\'SDisease': 'ParkinsonsDisease',
            'ObstructiveSleepApneaSyndrome': 'ObstructiveSleepApnea',
            'BCellAcuteLymphoblasticLeukemia': 'AcuteLymphoblasticLeukemia',
            'HepatitisCInfection': 'HepatitisC',
            # Cell Type
            'OlfactoryProjectionNeuronInnervatingDA1,VA1DOrDC3Glomerulus': 'OlfatoryProjectionNeuron',
            'OlfactoryProjectionNeuron': 'OlfatoryProjectionNeuron',
            'NeutrophilAndMyeloidCell': ['Neutrophil', 'MyeloidCell'],
            'AdiposeTissueDerivedMesenchymalStemCell': 'MesenchymalStemCellOfAdipose',
            'MatureTCell': 'MatureTcell',
            'ThymicTCell': 'ThymicTcell',
            'HematopoieticStemCellAndThrombocyte': ['HematopoieticStemCell', 'Thrombocyte'],
            'EmbryonicNeuralBorderStemCell': 'EmbryonicStemCell',
            'Multi-LymphoidProgenitor': 'CommonLymphoidProgenitor',
            'PlantProtoplast': 'Protoplast',
            'CD8-PositiveT-Lymphocytes': 'CD8+AlphaBetaTcell',
            'CD8-Positive,Alpha-BetaTCell': 'CD8+AlphaBetaTcell',
            'MemoryBCell': 'MemoryBcell',
            'BCell': 'MemoryBcell',
            'MouseEmbryonicStemCell': 'EmbryonicStemCell',
            'HematopoieticStemCellAndThrombocyte': ['HematopoieticStemCell', 'Thrombocyte'],
            'Un-CryopreservedPeripheralBloodMononuclearCells(PBMCs)': 'PeripheralBloodMononuclearCell',
            'Lymphoid-PrimedMultipotentProgenitor': 'EarlyLymphoidProgenitor',
            'MixOfStromalFibroblastsAndEpithelialTumourCells': ['Fibroblast', 'EpithelialTumorCell'],
            'GranulocyteMacrophageProgenitor': 'GranulocyteMonocyteProgenitorCell',
            'Neuronal,GlialAndVascularCells': 'Neuron',
            'Marrow-DerivedBCell': 'MarrowDerivedBcell',
            'CD4-PositiveHelperTCell': 'CD4+HelperTcell',
            'HematopoieticStemCellAndHematopoieticMultipotentProgenitorCell': ['HematopoieticStemCell', 'HematopoieticMultipotentProgenitorCell'],
            'Pre-ConventionalDendriticCell': 'PreConventionalDendriticCell',
            'EpiblastCell': 'Epiblast',
            'MedialGanglionicEminence': 'GanglionicEminence',
            'NaiveThymus-DerivedCD4-Positive,Alpha-BetaTCell': 'NaiveThymusDerivedCD4+AlphaBetaTcell',
            'NeuralCrest-DerivedCell': 'NeuralCrestDerivedCell',
            'CardiacNon-Myocyte': 'CardiacNonMyocyte',
            'TransitionalStageBCell': 'TransitionalStageBcell',
            'NaiveBCell': 'NaiveBcell',
            'CD4-Positive,CD25-Positive,Alpha-BetaRegulatoryTCell': 'CD4+CD25+AlphaBetaRegulatoryTcell',
            'ExtraThymicAire-ExpressingCells': 'ExtraThymicAireExpressingCells',
            'GranulocyteMonocyteProgenitor': 'GranulocyteMonocyteProgenitorCell',
            'MarrowDerivedBCell': 'MarrowDerivedBcell',
            'InvasiveFront': 'Front',
            'Testis': 'Testes',
            'PosteriorIliacCrest': 'IliacCrest',
            # Preservation
            'FreshSpecimen': 'Fresh',
            # Library
            'Smart-Seq': 'Smart-seq',
            'Smart-Like': 'Smart-like',
            '10Xv2': '10Xv2Sequencing',
            'MixedPedalDigit3AndPedalDigit4': 'PedalDigit',
            'Digit4': 'PedalDigit',
            'Drop-Seq': 'Drop-seq',
            'Smart-Seq2': 'Smart-seq2',
            'Seq-Well': 'Seq-well',
            '10X5Prime': '10X5v2Sequencing',
            '10Xv3': '10xv3Sequencing',
            # Stage
            '2-CellStageEmbryo': '2CellStageEmbryo',
            '4-CellStageEmbryo': '4CellStageEmbryo',
            '8-CellStageEmbryo': '8CellStageEmbryo',
            'MorulaCell': 'Morula',

        }
        return mapping_dict

    def format_concrete_specimen(self, raw_specimen, specimen_id):
        pass

    def format_concrete_project(self, raw_project, project_id):

        project = Project(project_id)

        project.part_of_repository = "SingleCellExpresionAtlas"

        project.project_id = raw_project['experimentAccession']
        project.project_title = raw_project['experimentDescription']
        project.specie = self.parse_word(raw_project['species'])
        project.load_date = raw_project['loadDate']
        project.update_date = raw_project['lastUpdate']
        project.total_cell_counts = raw_project['numberOfAssays']
        project.type = self.parse_word(raw_project['experimentType'])
        project.library = self.parse_word(raw_project['technologyType'])
        project.experimental_factor = self.parse_word(raw_project['experimentalFactors'])

        project.part_of_collection = self.parse_word(raw_project['experimentProjects'])
        project.supplementary_link = raw_project['supplementary_link']
        project.repository_link = raw_project['repository_link']
        project.publication_title = raw_project['publication_title']
        project.publication_link = raw_project['publication_link']
        project.array_express_id = raw_project['ArrayExpress_ID']
        project.ena_id = raw_project['ENA_ID']

        project = self.__project_info_to_project(project, raw_project['project_info'])

        project.downloads_type = self.parse_word(self.__get_download_types(raw_project))

        self.project = project

    def parse_concrete(self, word):
        aux = list(word.title())

        for i in range(len(word)):
            if word[i].isupper():
                aux[i] = word[i]

        aux = ''.join(aux).replace(' ', '')

        return aux

    def __get_download_types(self, raw_project):
        types = set()

        for download in raw_project['downloads']:
            for file in download['files']:
                if file['isDownload']:
                    description = file['description']
                    types.add(description)

        return list(types)

    def __project_info_to_project(self, project, project_info):
        sample_characteristics = project_info['sample_characteristics']
        experimental_variables = project_info['experimental_variables']

        for key in sample_characteristics:
            if key == 'organism':
                project.specie = self.parse_word(sample_characteristics[key])
            elif key == 'age' or key == 'post conception age':
                project.min_age, project.max_age, project.age_unit = self.__process_age(sample_characteristics[key])
            elif key == 'sex':
                project.biological_sex = self.map_word(sample_characteristics[key])
            elif key == 'organism part':
                project.organism_part = self.parse_word(sample_characteristics[key])
            elif key == 'metastatic site':
                project.metastatic_site = self.parse_word(sample_characteristics[key])
            elif key == 'sampling site' or key == 'biopsy site':
                project.biopsy_site = self.parse_word(sample_characteristics[key])
            elif key == 'disease':
                disease = self.parse_word(sample_characteristics[key])
                disease = norm2control(disease)
                project.disease = disease
            elif key == 'cell type':
                project.cell_type = self.parse_word(sample_characteristics[key])
            elif key == 'biosource provider' or key == 'biomaterial_provi':
                project.laboratory = sample_characteristics[key]
            elif key == 'specimen with known storage state':
                project.preservation = self.parse_word(sample_characteristics[key])
            elif key == 'organismStatus':
                project.sample_status = sample_characteristics[key]
            else:
                continue

        return project

    def __process_age(self, age):
        if type(age) is list:
            age_list = list(map(self.__process_age, age))
            age_list = zip(*age_list)
            age_list = list(map(list, age_list))
            
            if len(set(age_list[0])) > 1:
                age_list[0] = [x for x in age_list[0] if x != -1]

            return min(age_list[0]), max(age_list[1]), age_list[2]

        min_age = -1
        max_age = -1
        age_unit = 'year'

        for word in age.split(' '):

            try:
                # Parse numbers
                age_number = int(word)
                if min_age == -1:
                    min_age = age_number
                else:
                    max_age = age_number
            except ValueError:
                # Parse strings
                if word == 'gestational':
                    age_unit = 'gestationalWeek'
                if word == 'week' and age_unit != 'gestationalWeek':
                    age_unit = word
                if word == 'embryonic':
                    age_unit = 'embryonicDay'
                if word == 'day' and age_unit != 'embryonicDay':
                    age_unit = 'day'
                if word == 'hour' or word == 'month':
                    age_unit = word
                if word == 'applicable':
                    age_unit = 'notApplicable'
                if word == 'available':
                    age_unit = 'notAvailable'
        if max_age == -1:
            max_age = min_age

        return min_age, max_age, age_unit
