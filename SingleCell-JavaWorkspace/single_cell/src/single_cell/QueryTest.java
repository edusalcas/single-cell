package single_cell;

import org.apache.jena.query.*;

public class QueryTest {

	private static void executeQuery(String NS, MyModel model, String queryStringTest7) {
		Query query = QueryFactory.create(queryStringTest7);
		try (QueryExecution qexec = QueryExecutionFactory.create(query, model.getModel())) {
			ResultSet results = qexec.execSelect();
			int i = 0;
			for (; results.hasNext();i++) {
				QuerySolution soln = results.nextSolution();
				
				System.out.println(soln.toString().replaceAll(NS, ""));
			}
			// System.out.println(i + " results.");
		}
	}
	
	public static void main(String[] args) {
		String inputFileName = "../../SingleCell-Files/out_repositoriev4.owl";

		String NS = "http://www.semanticweb.org/alicia/ontologies/2020/8/singleCellRepositories#";
		String rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#";
		String xsd = "http://www.w3.org/2001/XMLSchema#";
		
		MyModel model = new MyModel(NS, inputFileName);

		// -----------------------------
		// 2.2.3 ¿Qué tipos celulares se han seleccionado para estudiar la diabete de tipo 2? 
		// -----------------------------
		
		System.out.println();
		System.out.println("------------------------");
		System.out.println("2.2.6. ¿Tenemos datos de single-cell disponibles para un tipo de célula que sea específico de decidua y placenta?");
		System.out.println("------------------------");
		System.out.println();
		
		String projectTitle = "Melanoma infiltration of stromal and immune cells";
		
		String queryString = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"SELECT (COUNT( * ) as ?numberOfSpecimens) \n" +
				"WHERE" +
				"{" +
					"?specimen rdf:type a:Specimen ;" +
					"          a:SPR.hasProjectTitle \"" + projectTitle + "\" ." +
				"}";
		
		// Execute query
		// executeQuery(NS, model, query);
		
		
		Query query = QueryFactory.create(queryString);
		try (QueryExecution qexec = QueryExecutionFactory.create(query, model.getModel())) {
			ResultSet results = qexec.execSelect();
			int i = 0;
			
			QuerySolution soln = results.nextSolution();	
			
			System.out.println(soln.getLiteral("?numberOfSpecimens").getInt());
		}
		
	}
}
