package single_cell;

import java.util.List;

import org.json.JSONArray;
import org.json.JSONObject;

public class MyProject extends MyIndividual{

	public MyProject(JSONObject jsonIndividual, MyModel model) {
		super(jsonIndividual, model);
	}

	@Override
	protected String[] getObjectProperties() {
		return MyModel.OBJECT_PROPERTIES;
	}

	@Override
	protected String[] getDataProperties() {
		return MyModel.PROJECT_DATA_PROPERTIES;
	}
	
	@Override
	protected String[] getAnnotationProperties() {
		return MyModel.PROJECT_ANNOTATION_PROPERTIES;
	}
	
	@Override
	protected void createIndividual(String id) {
		getModel().createProject(id);
	}


}
