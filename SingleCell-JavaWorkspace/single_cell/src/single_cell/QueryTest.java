package single_cell;

import org.apache.jena.query.*;

public class QueryTest {

	public static void main(String[] args) {
		String inputFileName = "../../SingleCell-Files/out_repositoriev3.owl";

		String NS = "http://www.semanticweb.org/alicia/ontologies/2020/8/singleCellRepositories#";
		String rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#";
		String xsd = "http://www.w3.org/2001/XMLSchema#";
		
		MyModel model = new MyModel(NS, inputFileName);

		// Query for all individuals of one type
		String subject = "?id";
		String predicate = "<" + rdf + "type" + ">";
		String object = "<" + NS + "10xv3sequencing" + ">";
		
		String queryStringBase = "SELECT " + subject + "\n" + 
				"WHERE\n" + 
				"{ " + subject + " " + predicate + " " + object + " .} ";
		
		// Query for all properties of one individual
		subject = "<" + NS + "F16_1" + ">";
		predicate = "?propertyName";
		object = "?propertyValue";
		
		String queryStringProp = "SELECT " + predicate + " " + object + "\n" + 
				"WHERE\n" + 
				"{ " + subject + " " + predicate + " " + object + " .} ";
				
		// Query with multiple triplets
		String queryStringMultiple = "PREFIX a: <" + NS + ">" +
				"PREFIX rdf: <" + rdf + ">" +
				"SELECT ?id ?sex ?age \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Blood ." +
					"?id a:hasBiologicalSexOf ?sex ." +
					"?id a:hasAgeOf ?age ." +
				"}";
		
		// Query to find data that doesnt meet a condition
		String queryStringMiss = "PREFIX a: <" + NS + ">" +
				"PREFIX rdf: <" + rdf + ">" +
				"SELECT ?id \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Project ." +
					"MINUS { ?id rdf:type a:Organ }" +
				"}";
		
		// Query with distinct
		String queryStringDist = "PREFIX a: <" + NS + ">" +
				"PREFIX rdf: <" + rdf + ">" +
				"SELECT DISTINCT ?organ \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Organ ;" +
					"    rdf:type ?organ ." +
				"}";
		
		// Query "datos ATAC-seq de single cell de ratón, en sangre periférica"
		
		String queryStringTest1 = "PREFIX a: <" + NS + ">" +
				"PREFIX rdf: <" + rdf + ">" +
				"SELECT ?id ?cellType ?disease \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Sample ;" +
					"    a:SR.hasGenusSpecie a:HomoSapiens ;" +
					"    a:SR.hasLibrary a:Smart-seq2 ;" +
					"    a:SR.hasSelectedCellType ?cellType ;" +
					"    a:SR.hasDiseaseStatus ?disease ;" +
				"}";
		
		// Query "expresión de genes de single cell de humano, en adultos mayores de 40 años, en la región cerebral del cortex, 
		// y con enfermedad de Parkinson"
		
		String queryStringTest2 = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?id ?minAge ?maxAge ?object \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Sample ;" +
					"    a:SR.hasGenusSpecie a:HomoSapiens ;" +
					"    a:SR.hasDiseaseStatus a:ProstateCancer ;" +
					"    a:hasMinAge ?minAge ;" +
					"    a:hasMaxAge ?maxAge ;" +
					"    a:SR.hasObjectOfStudy ?object ;" +
				"}";
				
		
		// Query "expresión de genes de neuronas excitatorias de nivel 6 en humanos"
		
		String queryStringTest3 = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?id \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:DiseaseStatus ;" +
					"    a:OR.hasAffected a:Skin" +
				"}";
		
		// Execute query
		Query query = QueryFactory.create(queryStringTest3);
		try (QueryExecution qexec = QueryExecutionFactory.create(query, model.getModel())) {
			ResultSet results = qexec.execSelect();
			int i = 0;
			for (; results.hasNext();i++) {
				QuerySolution soln = results.nextSolution();
				
				System.out.println("Match: " + soln.toString().replaceAll(NS, ""));
			}
			System.out.println(i + " results.");
		}
	}
}
