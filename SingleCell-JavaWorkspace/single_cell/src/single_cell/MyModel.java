package single_cell;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

import org.apache.jena.ontology.Individual;
import org.apache.jena.ontology.ObjectProperty;
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
	private HashMap<String, Property> dataPropertyMap;
	private HashMap<String, ObjectProperty> objectPropertyMap;
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
			"belongsToKingdom",
			"hasAnalysisProtocol",
			"hasCellLineType",
			"hasDiseaseStatus",
			"hasFileType",
			"hasGenusSpecie",
			"hasInstrument",
			"hasLibrary",
			"hasModelOrgan",
			"hasOrgan",
			"hasOrganPart",
			"hasPreservation",
			"hasSampleType",
			"hasSelectedCellType",
			"isPartOfCollection",
			"isPartOfProject",
			"isPartOfRepository"
	};
	
	public static final String[] DATA_PROPERTIES = new String[] {
			"hasAge",
			"hasAgeRange",
			"hasAgeUnit",
			"hasBiologicalSex",
			"hasLaboratory",
			"hasProjectShortName",
			"hasProjectTitle",
			"hasTotalCellCounts",
			"hasTotalDonorCounts",
			"hasTotalSize",
			"isPairedEnd"
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
		dataPropertyMap = new HashMap<>();
		objectPropertyMap = new HashMap<>();
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

			if (ontClass == null)
				System.err.println("Warning: Class " + className + " is not in the ontology model.");
			
		}
		return ontClass;
	}

	public Property getDataProperty(String propertyName) {
		Property property = dataPropertyMap.get(propertyName);

		if (!dataPropertyMap.containsKey(propertyName)) {
				property = model.getProperty(NS + propertyName);
				dataPropertyMap.put(propertyName, property);
				
				if (property == null) 
					System.err.println("Warning: Data property " + propertyName + " is not in the ontology model.");
		}
		return property;
	}
	
	public ObjectProperty getObjectProperty(String propertyName) {
		ObjectProperty property = objectPropertyMap.get(propertyName);

		if (!objectPropertyMap.containsKey(propertyName)) {
			property = model.getObjectProperty(NS + propertyName);
			objectPropertyMap.put(propertyName, property);
			
			if (property == null) 
				System.err.println("Warning: Object property " + propertyName + " is not in the ontology model.");
		}
		return property;
	}
	
	public void addClassToIndividual(String subject, String predicate, Object object) {
		OntClass ontClass = getOntClass(object.toString());
		Individual individual = model.createIndividual(NS + subject, ontClass);
		if (!individualMap.containsKey(subject))
			individualMap.put(subject, individual);
	}
	
	public void addDataPropertyToIndividual(String subject, String predicate, Object object) {
		if (object.toString().compareTo("null") == 0)
			object = "unspecified";

		Property property = getDataProperty(predicate);
		Individual individual = individualMap.get(subject);
		model.add(individual, property, object.toString());
	}
	
	public void addObjectPropertyToIndividual(String subject, String predicate, Object object) {
		if (object.toString().compareTo("null") == 0)
			object = "unspecified";
		
		ObjectProperty property = getObjectProperty(predicate);
		Individual individual = individualMap.get(subject);
		model.add(individual, property, object.toString());
	}
	
	public Model getModel() {
		return model;
	}



}
