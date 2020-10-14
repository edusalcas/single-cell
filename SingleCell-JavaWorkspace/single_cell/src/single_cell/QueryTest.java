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
		
		// Que enfermedad tienen y que tipo de celula tienen los individuos que son persona y han usado la librería Smart-seq2
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
		
		// La edad y el objeto de estudio de las personas con cancer de próstata
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
				
		
		// Enfermedades que afectan a la piel
		String queryStringTest3 = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?id \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:DiseaseStatus ;" +
					"    a:OR.hasAffected a:Skin" +
				"}";
		
		// Todos los individuos que tengan una enfermedad del tipo "DiseaseOfAnatomicalEntity" (inferencia)
		String queryStringTest4 = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?id ?specie ?disease \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Sample ;" +
					"    a:SR.hasGenusSpecie ?specie ;" +
					"    a:SR.hasDiseaseStatus ?disease ." +
					"?disease rdf:type a:DiseaseOfAnatomicalEntity ." +
				"}";
		
		// Cuenta los individuos que son mujeres y tienen 50 años o más
		String queryStringTest5 = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (COUNT(*) as ?total) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Sample ;" +
					"    a:SR.hasGenusSpecie a:HomoSapiens ;" +
					"    a:hasBiologicalSex ?sex ;" +
					"    a:hasMinAge ?minAge ." +
					"FILTER (?minAge >= 50) ." +
					"FILTER (?sex = \"female\") ." +
				"}";
		
		// Muestra todos los proyectos y cuantos samples tiene cada uno
		String queryStringTest6 = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?project (COUNT(*) as ?total) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Sample ;" +
					"    a:hasProjectShortName ?project ." +
				"}" +
				"GROUP BY ?project";
				
		
		// Execute query
		Query query = QueryFactory.create(queryStringTest6);
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
