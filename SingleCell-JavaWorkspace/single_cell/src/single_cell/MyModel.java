package single_cell;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

import org.apache.jena.ontology.Individual;
import org.apache.jena.ontology.OntClass;
import org.apache.jena.ontology.OntModel;
import org.apache.jena.ontology.OntModelSpec;
import org.apache.jena.ontology.OntProperty;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;

public class MyModel {
	private OntModel model;
	private String NS;
	private FileInputStream inputStream;
	private FileOutputStream outputStream;

	private HashMap<String, OntClass> classMap;
	private HashMap<String, Property> propertyMap;
	private HashMap<String, Individual> individualMap;

	public static final String PREDICATE_CLASS = "Type";

	public static final String[] CLASSES = new String[] {
			"Accesion",
			"Collection",
			"Disease",
			"Experimental",
			"FileFormat",
			"FileType",
			"GenusSpecies",
			"Kingdom",
			"AnalysisProtocol",
			"InstrumentModel",
			"Library",
			"Preservation",
			"Organ",
			"OrganPart",
			"CellType",
			// "Repository",
			"SampleType"
	};
	
	public static final String[] OBJECT_PROPERTIES = new String[] {
			"hasAccessIdIn",
			"hasAnalysisProtocolOf",
			"hasCellLineType",
			"hasDiseaseStatusOf",
			"hasFileTypeOf",
			"hasInstrumentOf",
			"hasLibraryOf",
			"hasModelOrganOf",
			"hasOrganOf",
			"hasOrganPartOf",
			"hasPreservationOf",
			"hasSampleTypeOf",
			"hasSelectedCellTypeOf",
			"isComposedOf",
			"isPartOfCollection",
			"isPartOfProject",
			"isPartOfRepository"
	};
	
	public static final String[] DATA_PROPERTIES = new String[] {
			"hasAccessId",
			"hasAgeOf",
			"hasAgeRangeOf",
			"hasAgeUnitOf",
			"hasBiologicalSexOf",
			"hasCellCountsEstimatesOf",
			"hasDonorCountOf",
			"hasProjectTitle",
			"hasProjectShortName",
			"hasSizeOf",
			"hasTotalCellsOf",
			"hasTotalDonorCounts",
			"hasTotalSizeOf",
			"isPairedEnd",
			"isPartOfLaboratory"
	};
	
	private void initializeInputStream(String inputFileName) {
		try {
			inputStream = new FileInputStream(inputFileName);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	private void initializeOutputStream(String outputFileName) {
		try {
			outputStream = new FileOutputStream(outputFileName);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public MyModel(String NS, String inputFileName) {
		this.NS = NS;

		initializeInputStream(inputFileName);

		model = ModelFactory.createOntologyModel(OntModelSpec.OWL_MEM_RULE_INF);

		model.read(inputStream, "RDF/XML");

		classMap = new HashMap<>();
		propertyMap = new HashMap<>();
		individualMap = new HashMap<>();
		
		classMap.put(null, null);
	}

	public void saveModel(String outputFileName) {
		initializeOutputStream(outputFileName);
		
		model.write(outputStream, "RDF/XML");
	}

	public OntClass getOntClass(String className) {		
		OntClass ontClass = classMap.get(className);

		if (!classMap.containsKey(className)) {
			ontClass = model.getOntClass(NS + className);
			classMap.put(className, ontClass);

			if (ontClass == null) {
				System.err.println("Warning: Class " + className + " is not in the ontology model.");
			}
			
		}
		return ontClass;
	}

	public Property getProperty(String propertyName) {
		Property property = propertyMap.get(propertyName);

		if (property == null) {
			try {
				property = model.getProperty(NS + propertyName);
				propertyMap.put(propertyName, property);
			} catch (Exception e) {
				System.err.println("Warning: Property " + propertyName + " is not in the ontology model.");
			}
		}
		return property;
	}

	public void createIndividual(String subject, String predicate, String object) {
		if (predicate == PREDICATE_CLASS) {
			OntClass ontClass = getOntClass(object);
			Individual individual = model.createIndividual(NS + subject, ontClass);
			if (!individualMap.containsKey(subject))
				individualMap.put(subject, individual);
		} else {
			Property property = getProperty(predicate);
			Individual ind = individualMap.get(subject);
			ind.addProperty(property, object);
		}
		
	}
	
	public void createIndividual(String subject, String predicate, Long object) {
		Property property = getProperty(predicate);
		Individual ind = individualMap.get(subject);
		ind.addProperty(property, object.toString());		
	}
	
	public void createIndividual(String subject, String predicate, Boolean object) {
		Property property = getProperty(predicate);
		Individual ind = individualMap.get(subject);
		ind.addProperty(property, object.toString());		
	}

	public void createIndividual(String subject, String predicate, Integer object) {
		Property property = getProperty(predicate);
		Individual ind = individualMap.get(subject);
		ind.addProperty(property, object.toString());		
	}
	
	public void createIndividual(String subject, String predicate, Map object) {
		Property property = getProperty(predicate);
		Individual ind = individualMap.get(subject);
		ind.addProperty(property, object.toString());		
	}

	public Model getModel() {
		return model;
	}



}
