package single_cell;

import org.json.JSONObject;

public class MySpecimen extends MyIndividual {

	public MySpecimen(JSONObject jsonIndividual, MyModel model) {
		super(jsonIndividual, model);
	}

	@Override
	protected String[] getObjectProperties() {
		return MyModel.OBJECT_PROPERTIES;
	}

	@Override
	protected String[] getDataProperties() {
		return MyModel.SPECIMEN_DATA_PROPERTIES;
	}

}
