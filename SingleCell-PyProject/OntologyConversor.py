import json
import sys

mappingDic = {
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
    'Smart-Seq2': 'Smart-seq2',
    'Sci-RNA-Seq': 'Sci-RNA-seq',
    'MARS-Seq': 'MARS-seq',
    'CEL-Seq2': 'CEL-seq2',
    'CITE-Seq': 'CITE-seq',
    'CD8-Positive,Alpha-BetaTCell': 'CD8-positive_Alpha-betaTcell',
    'CD11B+CD11C+DC': 'CD11b+CD11c+DC',
    'CD11C+DC': 'CD11c+DC',
    'CD11B+Macrophages/Monocytes': 'CD11b+Macrophages/monocytes',
    'CD34-Positive,CD38-NegativeHematopoieticStemCell': 'CD34-positive_CD38-negative_HematopoieticStemCell',
    'EffectorMemoryCD8-Positive,Alpha-BetaTCell,TerminallyDifferentiated': 'EffectorMemoryCD8-positive_Alpha-betaTCell_TerminallyDifferentiated',
    '10XV2Sequencing': '10Xv2Sequencing',
    '10XV3Sequencing': '10xv3Sequencing',
    "10X3'V1Sequencing": "10X3'v1Sequencing",
    "10X3'V2Sequencing": "10X3'v2Sequencing",
    "10X3'V3Sequencing": "10x3'v3Sequencing",
    "10X5'V2Sequencing": "10X5'v2Sequencing",
    # 'DNALibraryConstruction': '',
    # 'CDNALibraryConstruction': '',
    'BladderOrgan': 'Bladder',
    'MuscleOrgan': 'Muscle',
    'Cryopreservation,Other': 'CryopreservationOther',
    'CryopreservationInLiquidNitrogen(DeadTissue)': 'CryopreservationInLiquidNitrogenDeadTissue',
    'Optimus_V1.3.1': 'Optimus_v1.3.1',
    'Optimus_V1.3.2': 'Optimus_v1.3.2',
    'Optimus_V1.3.3': 'Optimus_v1.3.3',
    'Optimus_V1.3.5': 'Optimus_v1.3.5',
    'Smartseq2_V2.3.0': 'Smartseq2_v2.3.0',
    'Smartseq2_V2.4.0': 'Smartseq2_v2.4.0',
}


####################################################
# Auxiliar functions
####################################################

def hca2ont(text):
    if text is None:
        return None

    # If text is a list, apply hca2ont for each item
    if type(text) is list:
        return list(map(hca2ont, text))

    aux = list(text.title())

    for i in range(len(text)):
        if text[i].isupper():
            aux[i] = text[i]

    aux = ''.join(aux).replace(' ', '')

    try:
        aux2 = mappingDic[aux]
        return aux2
    except KeyError:
        return aux


def init_individual():
    individual = {
        # Cell Lines
        'cell_line_type': None,
        'model_organ': None,
        # Cell Suspensions
        'organ': None,
        'organ_part': None,
        'selected_cell_type': None,
        'total_cells': None,
        # Donor Organism
        'biological_sex': None,
        'disease': None,
        'donor_count': None,
        'genus_species': None,
        'organism_age': None,
        'organism_age_range': None,
        'organism_age_unit': None,
        # Entry Id
        # File Type Summaries
        'count': None,
        'file_type': None,
        'total_size': None,
        # Organoids
        'model_organ_part': None,
        # Projects
        'laboratory': None,
        'project_shortname': None,
        'project_title': None,
        # Protocols
        'instrument_manufacturer_model': None,
        'library_construction_approach': None,
        'paired_end': None,
        # Samples
        'sample_entity_type': None,
        # Specimens
        'id': None,
        'preservation_method': None

    }

    individual = {
        "ID": None,
        "Classes": {
            "Accesion": None,
            "Collection": None,
            "Disease": None,
            "Experimental": None,
            "FileFormat": None,
            "FileType": None,
            "GenusSpecies": None,
            "Kingdom": None,
            "AnalysisProtocol": None,
            "InstrumentModel": None,
            "Library": None,
            "Preservation": None,
            "Organ": None,
            "OrganPart": None,
            "CellType": None,
            "Repository": None,
            "SampleType": None,
        },
        "ObjectProperties": {
            "hasAccessIdIn": None,
            "hasAnalysisProtocolOf": None,
            "hasCellLineType": None,
            "hasDiseaseStatusOf": None,
            "hasFileTypeOf": None,
            "hasInstrumentOf": None,
            "hasLibraryOf": None,
            "hasModelOrganOf": None,
            "hasOrganOf": None,
            "hasOrganPartOf": None,
            "hasPreservationOf": None,
            "hasSampleTypeOf": None,
            "hasSelectedCellTypeOf": None,
            "isComposedOf": None,
            "isPartOfCollection": None,
            "isPartOfProject": None,
            "isPartOfRepository": None
        },
        "DataProperties": {
            "hasAccessId": None,
            "hasAgeOf": None,
            "hasAgeRangeOf": None,
            "hasAgeUnitOf": None,
            "hasBiologicalSexOf": None,
            "hasCellCountsEstimatesOf": None,
            "hasDonorCountOf": None,
            "hasProjectTitle": None,
            "hasProjectShortName": None,
            "hasSizeOf": None,
            "hasTotalCellsOf": None,
            "hasTotalDonorCounts": None,
            "hasTotalSizeOf": None,
            "isPairedEnd": None,
            "isPartOfLaboratory": None,
        }
    }

    return individual


####################################################
# Main function
####################################################


def format_HCD(individual_hcd):
    individual = init_individual()

    individual['Classes']['Collection'] = ["HumanCellAtlas"]

    # Cell Lines
    individual = format_HCD_cell_lines(individual, individual_hcd)

    # Cell Suspensions
    individual = format_HCD_cell_suspensions(individual, individual_hcd)

    # Donor Organism
    individual = format_HCD_donor_organism(individual, individual_hcd)

    # File Type Summaries
    individual = format_HCD_file_type_summaries(individual, individual_hcd)

    # Organoids
    individual = format_HCD_organoids(individual, individual_hcd)

    # Projects
    individual = format_HCD_projects(individual, individual_hcd)

    # Protocols
    individual = format_HCD_protocols(individual, individual_hcd)

    # Samples
    individual = format_HCD_samples(individual, individual_hcd)

    # Specimens
    individual = format_HCD_specimens(individual, individual_hcd)

    return individual


####################################################
# Main function parts
####################################################

def format_HCD_cell_lines(individual, individual_hcd):
    if not individual_hcd['cellLines']:
        return individual

    cell_line_type = individual_hcd['cellLines'][0]['cellLineType']
    model_organ = individual_hcd['cellLines'][0]['modelOrgan']

    individual['Classes']['SampleType'] = [hca2ont(cell_line_type)]
    individual['ObjectProperties']['hasCellLineType'] = hca2ont(cell_line_type)
    individual['ObjectProperties']['hasModelOrganOf'] = hca2ont(model_organ)

    return individual


def format_HCD_cell_suspensions(individual, individual_hcd):
    if not individual_hcd['cellSuspensions']:
        return individual

    organ = individual_hcd['cellSuspensions'][0]['organ']
    organ_part = individual_hcd['cellSuspensions'][0]['organPart']
    selected_cell_type = individual_hcd['cellSuspensions'][0]['selectedCellType']
    total_cells = individual_hcd['cellSuspensions'][0]['totalCells']

    individual['Classes']['Organ'] = hca2ont(organ)
    individual['ObjectProperties']['hasOrganOf'] = hca2ont(organ)
    individual['Classes']['OrganPart'] = hca2ont(organ_part)
    individual['ObjectProperties']['hasOrganPartOf'] = hca2ont(organ_part)
    individual['Classes']['CellType'] = hca2ont(selected_cell_type)

    individual['DataProperties']['hasTotalCellsOf'] = total_cells

    return individual


def format_HCD_donor_organism(individual, individual_hcd):
    if not individual_hcd['donorOrganisms']:
        return individual

    biological_sex = individual_hcd['donorOrganisms'][0]['biologicalSex']
    disease = individual_hcd['donorOrganisms'][0]['disease']
    donor_count = individual_hcd['donorOrganisms'][0]['donorCount']
    genus_species = individual_hcd['donorOrganisms'][0]['genusSpecies']
    organism_age = individual_hcd['donorOrganisms'][0]['organismAge']
    organism_age_range = individual_hcd['donorOrganisms'][0]['organismAgeRange']
    organism_age_unit = individual_hcd['donorOrganisms'][0]['organismAgeUnit']

    individual['DataProperties']['hasBiologicalSexOf'] = hca2ont(biological_sex)
    individual['Classes']['Disease'] = hca2ont(disease)
    individual['DataProperties']['hasDonorCountOf'] = donor_count
    individual['Classes']['GenusSpecies'] = hca2ont(genus_species)
    individual['DataProperties']['hasAgeOf'] = organism_age
    individual['DataProperties']['hasAgeRangeOf'] = organism_age_range
    individual['DataProperties']['hasAgeUnitOf'] = hca2ont(organism_age_unit)

    return individual


def format_HCD_file_type_summaries(individual, individual_hcd):
    if not individual_hcd['fileTypeSummaries']:
        return individual

    # It is possible that one individual has multiple files
    file_type = []
    count = []
    total_size = []

    for i in range(len(individual_hcd['fileTypeSummaries'])):
        file_type.append(individual_hcd['fileTypeSummaries'][i]['fileType'])
        count.append(individual_hcd['fileTypeSummaries'][i]['count'])
        total_size.append(individual_hcd['fileTypeSummaries'][i]['totalSize'])

    individual['Classes']['FileFormat'] = file_type
    individual['ObjectProperties']['hasFileTypeOf'] = file_type
    individual['DataProperties']['hasCellCountsEstimatesOf'] = count
    individual['DataProperties']['hasSizeOf'] = total_size
    individual['DataProperties']['hasTotalSizeOf'] = sum(total_size)

    return individual


def format_HCD_organoids(individual, individual_hcd):
    if not individual_hcd['organoids']:
        return individual

    model_organ = individual_hcd['organoids'][0]['modelOrgan']

    individual['ObjectProperties']['hasModelOrganOf'] = hca2ont(model_organ)

    return individual


def format_HCD_projects(individual, individual_hcd):
    if not individual_hcd['projects']:
        return individual

    laboratory = individual_hcd['projects'][0]['laboratory']
    project_shortname = individual_hcd['projects'][0]['projectShortname']
    project_title = individual_hcd['projects'][0]['projectTitle']

    individual['Classes']['Repository'] = hca2ont(laboratory)
    individual['DataProperties']['hasProjectShortName'] = project_shortname
    individual['DataProperties']['hasProjectTitle'] = project_title

    return individual


def format_HCD_protocols(individual, individual_hcd):
    if not individual_hcd['protocols']:
        return individual

    instrument_manufacturer_model = individual_hcd['protocols'][0]['instrumentManufacturerModel']
    library_construction_approach = individual_hcd['protocols'][0]['libraryConstructionApproach']
    paired_end = individual_hcd['protocols'][0]['pairedEnd']
    workflow = individual_hcd['protocols'][0]['workflow']

    individual['Classes']['InstrumentModel'] = hca2ont(instrument_manufacturer_model)
    individual['ObjectProperties']['hasInstrumentOf'] = hca2ont(instrument_manufacturer_model)
    individual['Classes']['Library'] = hca2ont(library_construction_approach)
    individual['ObjectProperties']['hasLibraryOf'] = hca2ont(library_construction_approach)
    individual['DataProperties']['isPairedEnd'] = paired_end
    individual['Classes']['AnalysisProtocol'] = hca2ont(workflow)
    individual['ObjectProperties']['hasAnalysisProtocolOf'] = hca2ont(workflow)

    return individual


def format_HCD_samples(individual, individual_hcd):
    if not individual_hcd['samples']:
        return individual

    sample_entity_type = individual_hcd['samples'][0]['sampleEntityType']

    individual['Classes']['SampleType'] = [hca2ont(sample_entity_type)]

    try:
        preservation_method = individual_hcd['samples'][0]['preservationMethod']
        individual['Classes']['Preservation'] = hca2ont(preservation_method)

        return individual
    except:
        return individual


def format_HCD_specimens(individual, individual_hcd):
    if not individual_hcd['specimens']:
        return individual

    individual_id = individual_hcd['specimens'][0]['id'][0]
    organ = individual_hcd['specimens'][0]['organ']
    organ_part = individual_hcd['specimens'][0]['organPart']
    preservation_method = individual_hcd['specimens'][0]['preservationMethod']

    individual['ID'] = individual_id
    individual['Classes']['Organ'] = hca2ont(organ)
    individual['ObjectProperties']['hasOrganOf'] = hca2ont(organ)
    individual['Classes']['OrganPart'] = hca2ont(organ_part)
    individual['ObjectProperties']['hasOrganPartOf'] = hca2ont(organ_part)
    individual['Classes']['Preservation'] = hca2ont(preservation_method)

    return individual
