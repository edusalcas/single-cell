package single_cell;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;

public class QueryAlicia {
	
	public static void main(String[] args) {
		String inputFileName = "../../SingleCell-Files/out_repositoriev3.owl";

		String NS = "http://www.semanticweb.org/alicia/ontologies/2020/8/singleCellRepositories#";
		String rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#";
		String xsd = "http://www.w3.org/2001/XMLSchema#";
		
		MyModel model = new MyModel(NS, inputFileName);
		
		/* 1. COMPROBACIÓN
		 * En primer lugar, he pensado que podríamos hacer algunas consultas que nos permitan comprobar que hemos incluido 
		 * toda la información de la HCA, contando el número de proyectos, laboratorios, especímenes, recuento de células y tamaño 
		 * total de los ficheros en GB (también hay otra que incluye el número de ficheros, pero nosotros no lo hemos incluido, no 
		 * creo que sea relevante). También podríamos hacerlo para órganos aunque ya sepamos que no va a coincidir para tener un resumen
		 *  completo de las características de nuestro dataset!  (si vemos que hay mucha discrepancia, lo ideal sería  repetir la misma 
		 *  consulta para cada uno de los órganos del HCA).
		 *  
		 *  Una segunda propuesta sería, por ejemplo, sumar el tipo de células para los principales objetos de estudio: blood, kidney, 
		 *  bone, liver, brain, lung, pancreas, heart, immune system y skin.
		 */
		
		// -----------------------------
		// 1.1. Número de proyectos
		// -----------------------------
		String queryStringNumProyects = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (COUNT( DISTINCT ?proyect ) as ?numberOfProyects) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasProjectTitle ?proyect ." +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringNumProyects);
		
		// -----------------------------
		// 1.2. Número de laboratorios
		// -----------------------------
		String queryStringNumLabs = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (COUNT( DISTINCT ?lab ) as ?numberOfLabs) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasLaboratory ?lab ." +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringNumLabs);
		
		// -----------------------------
		// 1.3. Número de especímenes
		// -----------------------------
		String queryStringNumSpecimens = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (COUNT( DISTINCT ?specimen ) as ?numberOfSpecimens) \n" +
				"WHERE" +
				"{" +
					"?specimen rdf:type a:Specimen ." +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringNumSpecimens);
		
		// -----------------------------
		// 1.4. Número de células
		// -----------------------------
		String queryStringNumCells = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (SUM(?numCells) as ?numberOfCells) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasTotalCellCounts ?numCells ." +
					"FILTER (?numCells != -1)" +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringNumCells);
		
		// -----------------------------
		// 1.5. Tamaño total de ficheros
		// -----------------------------
		String queryStringTotalSize = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (SUM(?size)/1024 as ?totalSize) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasTotalSizeOfFiles ?size ." +
					"FILTER (?size != -1)" +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringTotalSize);
		
		// -----------------------------
		// 1.5. Número de órganos
		// -----------------------------
		String queryStringNumOrgans = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (COUNT( DISTINCT ?object ) as ?numberOfOrgans) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasObjectOfStudy ?object ." +
					"?object rdf:type a:Organ ." +
				"}" +
				"ORDER BY ?object";
		
		// Execute query
		executeQuery(NS, model, queryStringNumOrgans);
		
		// -----------------------------
		// 1.5. Número de células por objeto de estudio
		// -----------------------------
		System.out.println("--------------\nNúmero de células por objeto de estudio\n--------------");
		String queryStringNumCellsPerObject = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?object (SUM(?numCells) as ?numberOfCells) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasObjectOfStudy ?object ;" +
					"    a:hasTotalCellCounts ?numCells ." +
					"FILTER (?numCells != -1)" +
				"}" +
				"GROUP BY ?object";
		
		// Execute query
		executeQuery(NS, model, queryStringNumCellsPerObject);
		
		String queryStringNumCellsPerModel = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?model (SUM(?numCells) as ?numberOfCells) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasModelOrgan ?model ;" +
					"    a:hasTotalCellCounts ?numCells ." +
					"FILTER (?numCells != -1)" +
				"}" +
				"GROUP BY ?model";
		
		// Execute query
		executeQuery(NS, model, queryStringNumCellsPerModel);
		
	}

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

}
