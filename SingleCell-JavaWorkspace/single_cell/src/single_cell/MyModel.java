package single_cell;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;

import org.apache.jena.ontology.Individual;
import org.apache.jena.ontology.ObjectProperty;
import org.apache.jena.ontology.OntClass;
import org.apache.jena.ontology.OntModel;
import org.apache.jena.ontology.OntModelSpec;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.reasoner.ValidityReport;
import org.apache.jena.reasoner.ValidityReport.Report;

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
	public static final String SAMPLE_CLASS = "Sample";

	private final String validateLogFileName = "../../SingleCell-Files/validateLog.txt";
	
	public static final String[] OBJECT_PROPERTIES = new String[] {
			"SR.hasAnalysisProtocol",
			"SR.hasCellLineType",
			"SR.hasDiseaseStatus",
			"SR.hasGenusSpecie",
			"SR.hasInstrument",
			"SR.hasLibrary",
			"SR.hasObjectOfStudy",
			"SR.hasPreservation",
			"SR.hasSampleType",
			"SR.hasSelectedCellType"
	};
	
	public static final String[] DATA_PROPERTIES = new String[] {
			"hasAgeUnit",
			"hasBiologicalSex",
			"hasAvailableDownloadsFormat",
			"hasAvailableDownloadsType",
			"hasLaboratory",
			"hasMaxAge",
			"hasMinAge",
			"hasModelOrgan",
			"hasProjectShortName",
			"hasProjectTitle",
			"hasTotalCellCounts",
			"hasTotalSizeOfFiles",
			"isPairedEnd",
			"isPartOfCollection",
			"isPartOfRepository",
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
	
	public Individual getIndividual(String individualName) {
		Individual individual = individualMap.get(individualName);

		if (!individualMap.containsKey(individualName)) {
			individual = model.getIndividual(NS + individualName);
			individualMap.put(individualName, individual);
			
			if (individual == null) 
				System.err.println("Warning: Individual " + individualName + " is not in the ontology model.");
		}
		return individual;
	}
	
	public void createIndividual(String id) {
		OntClass sampleClass = getOntClass(SAMPLE_CLASS);
		Individual individual = model.createIndividual(NS + id, sampleClass);
		
		individualMap.put(id, individual);
	}
	
	public void addClassToIndividual(String subject, String predicate, Object object) {
		OntClass ontClass = getOntClass(object.toString());
		Individual individual = model.createIndividual(NS + subject, ontClass);
		if (!individualMap.containsKey(subject))
			individualMap.put(subject, individual);
	}
	
	public void addObjectPropertyToIndividual(String subject, String predicate, Object object) {
		if (object.toString().compareTo("null") == 0)
			return;
		
		ObjectProperty property = getObjectProperty(predicate);
		Individual individual = individualMap.get(subject);
		Individual objectIndividual = getIndividual(object.toString());
		
		if (objectIndividual == null)
			return;
		
		model.add(individual, property, objectIndividual);
	}
	
	
	public void addDataPropertyToIndividual(String subject, String predicate, Object object) {
		if (object.toString().compareTo("null") == 0)
			object = "unspecified";

		Property property = getDataProperty(predicate);
		Individual individual = individualMap.get(subject);
		
		if (object instanceof String)
			model.add(individual, property, object.toString());
		else if (object instanceof Double)
			model.addLiteral(individual, property, (double) object);
		else if (object instanceof Integer)
			model.addLiteral(individual, property, (int) object);
		else if (object instanceof Boolean)
			model.addLiteral(individual, property, (boolean) object);

	}
	
	public boolean validateModel() {
		FileWriter writer = null;
		
		try {
			writer = new FileWriter(validateLogFileName);
		} catch (IOException e) {
			e.printStackTrace();
			return false;
		}
		
		System.out.println("Validating model...");
		
		ValidityReport validity = model.validate();
		
		if (validity.isValid()) {
			System.out.println("Model validated without errors.");
			return true;
		}
		
		System.out.println("Conflicts have occured during validation:");
		
		for (Iterator<Report> i = validity.getReports(); i.hasNext();) {
			ValidityReport.Report report = (ValidityReport.Report) i.next();
			
			try {
				writer.write(report.toString());
			} catch (IOException e) {
				e.printStackTrace();
				return false;
			}
			
			System.out.println(report);
		}
		
		return false;
	}
	
	public Model getModel() {
		return model;
	}

}
