package single_cell;

import java.io.IOException;

import org.json.*;

import java.nio.file.Files;
import java.nio.file.Path;

public class Test {

	private static String readJSON2String(String fileName) {
		Path fileNamePath = Path.of(fileName);
         
        String jsonContent = null;
		try {
			jsonContent = Files.readString(fileNamePath);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
		return jsonContent;
	}
	
	
	public static void main(String[] args) {
		
		// Declare variables and input/output streams
		String inputFileName = "../../SingleCell-Files/singleCellRepositoriesv4.owl";
		String outputFileName = "../../SingleCell-Files/out_repositoriev4.owl";
		String hitsFileName = "../../SingleCell-Files/processed_data/HCA_processed.json";
		
		String NS = "http://www.semanticweb.org/alicia/ontologies/2020/8/singleCellRepositories#";

		MyModel model = new MyModel(NS, inputFileName);

		// Read samples to introduce into the model as instances
		String rawJson = readJSON2String(hitsFileName);
		
		// Parse JSON to obtain the specimens and the projects
		JSONObject fullJson = new JSONObject(rawJson);
		JSONArray specimensArray = fullJson.getJSONArray("specimens");
		JSONArray projectsArray = fullJson.getJSONArray("projects");
				
		System.out.println("Adding specimens to model...");
		specimensArray.forEach((hit) -> {new MySpecimen((JSONObject) hit, model).addToModel();});
		System.out.println("Adding projects to model...");
		projectsArray.forEach((hit) -> {new MyProject((JSONObject) hit, model).addToModel();});

		// Check if model is valid
		if (!model.validateModel())
			;
		
		// Save the model with the instances
		model.saveModel(outputFileName);

	}

}


// TODO Add instances with subject-predicate-object structure
//if (flag) {
//	Resource subject = ResourceFactory.createResource("dummy/dummy");
//	Property predicate = RDF.type;
//	Resource object = ResourceFactory.createResource(NS + "HomoSapiens");
//	Statement statement = ResourceFactory.createStatement(subject, predicate, object);
//
//	model.add(statement);
//}
