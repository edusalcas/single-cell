from OntologyConversorAbstract import OntologyConversorAbstract
from Project import Project


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
            # Biopsy Site
            'Ascites': 'AsciticFluid',
            'LeftSupraclavicularLymphNode': 'LymphNode',
            'NotApplicable': 'NotApplicableSamplingSite',
            'AlveolusOfLung': 'Alveolus',
            'PrimaryTumor': 'Tumor',
            'NotApplicable': 'NotApplicableSamplingSite',
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
            'ColorectalCancer': 'ColorrectalCancer',
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
            'OlfactoryProjectionNeuronInnervatingDA1,VA1DOrDC3Glomerulus': 'OlfatoryNeuronProjection',
            'NeutrophilAndMyeloidCell': ['Neutrophil', 'MyeloidCell'],
            'AdiposeTissueDerivedMesenchymalStemCell': 'MesenchymalStemCellOfAdipose',
            'MatureTCell': 'MatureTcell',
            'ThymicTCell': 'ThymicTcell',
            'HematopoieticStemCellAndThrombocyte': ['HematopoieticStemCell', 'Thrombocyte'],
            'EmbryonicNeuralBorderStemCell': 'EmbryonicStemCell',
            'Multi-LymphoidProgenitor': 'CommonLymphoidProgenitor',
            'PlantProtoplast': 'Protoplast',
            'CD8-PositiveT-Lymphocytes': 'CD8+AlphaBetaTCell',
            'CD8-Positive,Alpha-BetaTCell': 'CD8+AlphaBetaTcell',
            'MemoryBCell': 'MemoryBcell',
            'BCell': 'MemoryBcell',
            'NotApplicable': 'NotApplicableCellType',
            'MouseEmbryonicStemCell': 'EmbryonicSte mCell',
            'HematopoieticStemCellAndThrombocyte': ['HematopoieticStemCell', 'Thrombocyte'],
            'Un-CryopreservedPeripheralBloodMononuclearCells(PBMCs)': 'PeripheralBloodMononuclearCell',
            'Lymphoid-PrimedMultipotentProgenitor': 'EarlyLymphoidProgenitor',
            'MixOfStromalFibroblastsAndEpithelialTumourCells': ['Fibroblasts', 'EpithelialTumorCell'],
            'GranulocyteMacrophageProgenitor': 'GranulocyteMonocyteProgenitor',
            'Neuronal,GlialAndVascularCells': 'Neuron',
            'Marrow-DerivedBCell': 'MarrowDerivedBCell',
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
            'CD4-Positive,CD25-Positive,Alpha-BetaRegulatoryTCell': 'CD4+_CD25+AlphaBetaRegulatoryTcell',
            'ExtraThymicAire-ExpressingCells': 'ExtraThymicAireExpressingCells',
            # Preservation
            'FreshSpecimen': 'Fresh',
            # Library
            'Smart-Seq': 'Smart-seq',
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
                # TODO
                continue
            elif key == 'sex':
                project.biological_sex = self.map_word(sample_characteristics[key])
            elif key == 'organism part':
                project.organism_part = self.parse_word(sample_characteristics[key])
            elif key == 'metastatic site' or key == 'sampling site' or key == 'biopsy site':
                project.biopsy_site = self.parse_word(sample_characteristics[key])
            elif key == 'disease':
                project.disease = self.parse_word(sample_characteristics[key])
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
