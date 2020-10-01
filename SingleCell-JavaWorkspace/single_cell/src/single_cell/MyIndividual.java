package single_cell;

import java.util.List;
import java.util.Map;

import org.apache.jena.ontology.Individual;
import org.apache.jena.ontology.OntClass;
import org.apache.jena.rdf.model.Property;
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

		OntClass classModel = model.getOntClass(className);

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
		
		// Add classes
		for (String className : MyModel.CLASSES) {
			try {
				List<Object> list = jsonIndividual.getJSONObject("Classes").getJSONArray(className).toList();
				for (Object ontClass : list) {
					model.createIndividual(id, MyModel.PREDICATE_CLASS, (String) ontClass);
				}
			} catch (Exception e) {
				// TODO: handle exception
			}

		}
		
		JSONObject objectProperties = jsonIndividual.getJSONObject("ObjectProperties");
		// Add object properties
		for (String propertyName : MyModel.OBJECT_PROPERTIES) {
			try {
				Object propertieValueObject = objectProperties.get(propertyName);
				
				if (propertieValueObject instanceof String) {
					
				} else if (propertieValueObject instanceof Long) {
					model.createIndividual(id, propertyName, (Long) propertieValueObject);
				} else if (propertieValueObject instanceof Integer) {
					model.createIndividual(id, propertyName, (Integer) propertieValueObject);
				} else if (propertieValueObject instanceof Boolean) {
					model.createIndividual(id, propertyName, (Boolean) propertieValueObject);
				} else if (propertieValueObject instanceof JSONArray) {
					List<Object> list = objectProperties.getJSONArray(propertyName).toList();
					for (Object propertyValue : list) {
						if (propertyValue instanceof String)
							model.createIndividual(id, propertyName, (String) propertyValue);
						else if (propertyValue instanceof Integer)
							model.createIndividual(id, propertyName, (Integer) propertyValue);
						else if (propertyValue instanceof Long)
							model.createIndividual(id, propertyName, (Long) propertyValue);
					    else if (propertyValue instanceof Boolean)
					    	model.createIndividual(id, propertyName, (Boolean) propertyValue);
					}
				} else {
					
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
				
				if (propertieValueObject instanceof String) {
					
				} else if (propertieValueObject instanceof Long) {
					model.createIndividual(id, propertyName, (Long) propertieValueObject);
				} else if (propertieValueObject instanceof Integer) {
					model.createIndividual(id, propertyName, (Integer) propertieValueObject);
				} else if (propertieValueObject instanceof Boolean) {
					model.createIndividual(id, propertyName, (Boolean) propertieValueObject);
				} else if (propertieValueObject instanceof JSONArray) {
					List<Object> list = dataProperties.getJSONArray(propertyName).toList();
					for (Object propertyValue : list) {
						if (propertyValue instanceof String)
							model.createIndividual(id, propertyName, (String) propertyValue);
						else if (propertyValue instanceof Integer)
							model.createIndividual(id, propertyName, (Integer) propertyValue);
						else if (propertyValue instanceof Long)
							model.createIndividual(id, propertyName, (Long) propertyValue);
					    else if (propertyValue instanceof Boolean)
					    	model.createIndividual(id, propertyName, (Boolean) propertyValue);
					    else if (propertyValue instanceof Map)
					    	model.createIndividual(id, propertyName, (Map) propertyValue);
					}
				} else {
					
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
