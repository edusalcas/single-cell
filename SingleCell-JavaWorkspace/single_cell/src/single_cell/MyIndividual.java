package single_cell;

import java.util.List;
import java.util.Map;

import org.apache.jena.ontology.Individual;
import org.apache.jena.ontology.OntClass;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;
import org.json.JSONArray;
import org.json.JSONObject;

public class MyIndividual {

	private String id;
	
	private JSONObject jsonIndividual;
	
	private Individual individual;
	private MyModel model;

	private String readStringFromJson(JSONObject jsonObject, String field) {
		String string = null;

		try {
			string = jsonObject.getString(field);
		} catch (Exception e) {
			return null;
		}

		return string;
	}

	private Integer readIntegerFromJson(JSONObject jsonObject, String field) {
		Integer integer = null;

		try {
			integer = jsonObject.getInt(field);
		} catch (Exception e) {
			return null;
		}

		return integer;
	}

	private void addClassToInd(String className) {
		if (className == null)
			return;

		Resource classModel = model.getOntClass(className);

		if (classModel == null)
			return;

		individual.addOntClass(classModel);
	}

	public MyIndividual(JSONObject jsonIndividual, MyModel model) {
		initIndividual(jsonIndividual);

		this.model = model;
	}

	private void initIndividual(JSONObject jsonIndividual) {

		this.id = readStringFromJson(jsonIndividual, "ID");
		
		this.jsonIndividual = jsonIndividual;
		
	}
	
	public Boolean addToModel() {
		
		model.createIndividual(id);
		
		JSONObject objectProperties = jsonIndividual.getJSONObject("ObjectProperties");
		// Add object properties
		for (String propertyName : MyModel.OBJECT_PROPERTIES) {
			try {
				Object propertieValueObject = objectProperties.get(propertyName);
				
				if (propertieValueObject instanceof JSONArray) {
					List<Object> list = objectProperties.getJSONArray(propertyName).toList();
					
					for (Object propertyValue : list) {
						if (propertyValue instanceof Object)
							model.addObjectPropertyToIndividual(id, propertyName, propertyValue);
					}
				} else if (propertieValueObject instanceof Object){
					model.addObjectPropertyToIndividual(id, propertyName, propertieValueObject);
				}
			} catch (Exception e) {
				e.printStackTrace();
				System.exit(1);
			}

		}
		
		JSONObject dataProperties = jsonIndividual.getJSONObject("DataProperties");
		// Add data properties
		for (String propertyName : MyModel.DATA_PROPERTIES) {
			try {
				Object propertieValueObject = dataProperties.get(propertyName);
				
				if (propertieValueObject instanceof JSONArray) {
					List<Object> list = dataProperties.getJSONArray(propertyName).toList();
					
					for (Object propertyValue : list) {
						if (propertyValue instanceof Object)
							model.addDataPropertyToIndividual(id, propertyName, propertyValue);
					}
				} else if (propertieValueObject instanceof Object){
					model.addDataPropertyToIndividual(id, propertyName, propertieValueObject);
				}
			} catch (Exception e) {
				e.printStackTrace();
				System.exit(1);
			}

		}
				
		// System.out.println("Individual " + id + " added to model.");

		return true;
	}


}
