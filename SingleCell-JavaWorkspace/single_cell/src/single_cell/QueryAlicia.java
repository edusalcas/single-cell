package single_cell;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;

public class QueryAlicia {
	
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
		System.out.println();
		System.out.println("------------------------");
		System.out.println("1.1. Número de proyectos");
		System.out.println("------------------------");
		System.out.println();

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
		System.out.println();
		System.out.println("------------------------");
		System.out.println("1.2. Número de laboratorios");
		System.out.println("------------------------");
		System.out.println();
		
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
		
		queryStringNumLabs = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?project ?lab \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasProjectTitle ?project ;" +
					"    a:hasLaboratory ?lab ." +
				"} " +
				"ORDER BY ?project";
		
		// Execute query
		executeQuery(NS, model, queryStringNumLabs);
		
		// -----------------------------
		// 1.3. Número de especímenes
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("1.3. Número de especímenes");
		System.out.println("------------------------");
		System.out.println();
		
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
		System.out.println();
		System.out.println("------------------------");
		System.out.println("1.4. Número de células");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringNumCells = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (SUM(?numCells)/1000000 as ?numberOfCells) \n" +
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
		System.out.println();
		System.out.println("------------------------");
		System.out.println("1.5. Tamaño total de ficheros");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringTotalSize = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (SUM(?size)/(1024 * 1024) as ?totalSize) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasTotalSizeOfFiles ?size ." +
					"FILTER (?size != -1) " +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringTotalSize);
		
		// -----------------------------
		// 1.6. Número de órganos
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("1.6. Número de órganos");
		System.out.println("------------------------");
		System.out.println();
		
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
		// 1.7. Número de células por objeto de estudio
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("1.7. Número de células por objeto de estudio");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringNumCellsPerObject = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?object (IF(SUM(?numCells) = 0, \"unspecified\", SUM(?numCells) / 1000) AS ?numTotalCells) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasObjectOfStudy ?object ;" +
					"    a:hasTotalCellCounts ?numCells ." +
					"FILTER (?numCells != -1)" +
				"}" +
				"GROUP BY ?object " +
				"ORDER BY ?object";
		
		// Execute query
		executeQuery(NS, model, queryStringNumCellsPerObject);
		
		// -----------------------------
		// 1.8. Número de células por proyecto
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("1.8. Número de células por proyecto");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringNumCellsPerProject = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?project (SUM(?numCells)/1000 as ?numberOfCells) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasProjectTitle ?project ;" +
					"    a:hasTotalCellCounts ?numCells ." +
					"FILTER (?numCells != -1) " +
				"}" +
				"GROUP BY ?project " +
				"ORDER BY ?project";
		
		// Execute query
		executeQuery(NS, model, queryStringNumCellsPerProject);
		
		/* 2. Consultas sencillas que podríamos hacer en HCA
		 * 
		 * a) Para conocer el repositorio
		 * 
		 * ¿Cuál es el laboratorio que más proyectos tiene y cuál es su principal órgano estudiado?
		 * ¿Cuál es el instrumento, el tipo de librería y el protocolo de análisis más utilizados en este repositorio?
		 * ¿De cuántos especímenes tenemos disponibles modelos de órganos y de qué órganos se trata? donde órgano me refiero como término de la HCA.
		 * ¿De cuántos especímenes tenemos disponibles datos de líneas celulares y para qué tipo de células?
		 * ¿Cuál es el órgano para el cual tenemos un mayor número de enfermedades estudiadas?
		 * ¿Cuál es el proyecto que tiene un mayor número de especímenes asociado? ¿y el mayor número de cell counts?
		 * 
		 * b) Como usuario que busca sobre un tema concreto
		 * 
		 * Si me interesa como "órgano" de estudio blood, ¿de qué tipos celulares hay datos de single-cell disponibles en HCA? Si en su lugar  tuviera interés en el "órgano"
		 * immune system, ¿de qué tipos celulares hay datos de single-cell disponibles en HCA? ¿Qué tipos celulares son coincidentes entre ambos órganos?
		 * ¿Sobre qué enfermedades puedo encontrar datos de single-cell para embrión de Homo Sapiens? ¿y Mus Musculus?
		 * ¿Tenemos datos de single-cell disponibles para un tipo de célula que sea específico de decidua y placenta? ¿Cuál es el título y laboratorio del proyecto?
		 */
		
		
		// -----------------------------
		// 2.1. Para conocer el repositorio
		// -----------------------------
		
		// -----------------------------
		// 2.1.2 ¿Cuál es el instrumento, el tipo de librería y el protocolo de análisis más utilizados en este repositorio?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("2.1.2. ¿Cuál es el instrumento, el tipo de librería y el protocolo de análisis más utilizados en este repositorio?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringMaxInstrument = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?instrument (COUNT(*) as ?numberOfOccurrences) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasInstrument ?instrument ." +
				"}" +
				"GROUP BY ?instrument \n" +
				"ORDER BY DESC(?numberOfOccurrences) \n" +
				"LIMIT 1";
		
		// Execute query
		executeQuery(NS, model, queryStringMaxInstrument);
		
		String queryStringMaxLibrary = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?library (COUNT(*) as ?numberOfOccurrences) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasLibrary ?library ." +
				"}" +
				"GROUP BY ?library \n" +
				"ORDER BY DESC(?numberOfOccurrences) \n" +
				"LIMIT 1";
		
		// Execute query
		executeQuery(NS, model, queryStringMaxLibrary);
		
		String queryStringMaxProtocol = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?protocol (COUNT(*) as ?numberOfOccurrences) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasAnalysisProtocol ?protocol ." +
				"}" +
				"GROUP BY ?protocol \n" +
				"ORDER BY DESC(?numberOfOccurrences) \n" +
				"LIMIT 1";
		
		// Execute query
		executeQuery(NS, model, queryStringMaxProtocol);
		
		// -----------------------------
		// 2.1.3 ¿De cuántos especímenes tenemos disponibles modelos de órganos y de qué órganos se trata?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("2.1.3. ¿De cuántos especímenes tenemos disponibles modelos de órganos y de qué órganos se trata?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringNumberOfModels = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (COUNT( ?model ) as ?numberOfModels) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasModelOrgan ?model ." +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringNumberOfModels);
		
		System.out.println();
		
		String queryStringModels = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?model ( COUNT(*) AS ?numberOfOccurrences) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasModelOrgan ?model ." +
				"}" +
				"GROUP BY ?model";
		
		// Execute query
		executeQuery(NS, model, queryStringModels);
		
		// -----------------------------
		// 2.1.4 ¿De cuántos especímenes tenemos disponibles datos de líneas celulares y para qué tipo de células?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("2.1.4. ¿De cuántos especímenes tenemos disponibles datos de líneas celulares y para qué tipo de células?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringNumberOfCellLines = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (COUNT( ?cellLine ) as ?numberOfSpecimensWithCellLine) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasCellLineType ?cellLine ." +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringNumberOfCellLines);
		
		System.out.println();
		
		String queryStringCellLines = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?cellLine (COUNT (*) AS ?numberOfOccurrences) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasCellLineType ?cellLine ." +
				"}" +
				"GROUP BY ?cellLine";
		
		// Execute query
		executeQuery(NS, model, queryStringCellLines);
		
		// -----------------------------
		// 2.1.6. ¿Cuál es el proyecto que tiene un mayor número de especímenes asociado? ¿y el mayor número de cell counts?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("2.1.6. ¿Cuál es el proyecto que tiene un mayor número de especímenes asociado? ¿y el mayor número de cell counts?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringProjectWithMostSpecimens = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?project (COUNT(*) as ?numberOfSpecimens) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasProjectShortName ?project ." +
				"}" +
				"GROUP BY ?project \n" +
				"ORDER BY DESC(?numberOfSpecimens) \n" +
				"LIMIT 1";
		
		// Execute query
		executeQuery(NS, model, queryStringProjectWithMostSpecimens);
		
		String queryStringProjectWithMostCells = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?project (SUM(?cells) as ?numberOfCells) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasProjectShortName ?project ;" +
					"    a:hasTotalCellCounts ?cells ." +
				"}" +
				"GROUP BY ?project \n" +
				"ORDER BY DESC(?numberOfCells) \n" +
				"LIMIT 1";
		
		// Execute query
		executeQuery(NS, model, queryStringProjectWithMostCells);
		
		// -----------------------------
		// 2.2. Como usuario que busca sobre un tema concreto
		// -----------------------------
		
		// -----------------------------
		// 2.2.1. Si me interesa como "órgano" de estudio blood, ¿de qué tipos celulares hay datos de single-cell disponibles en HCA?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("2.2.1. Si me interesa como \"órgano\" de estudio blood, ¿de qué tipos celulares hay datos de single-cell disponibles en HCA?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringBloodCellType = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?cellType \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasSampleID ?sampleId ;"+
					"    a:SR.hasObjectOfStudy a:Blood ;" +
					"    a:SR.hasSelectedCellType ?cellType ." +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringBloodCellType);
		
		// -----------------------------
		// 2.2.2. Interés en el "órgano" immune system, ¿de qué tipos celulares hay datos de single-cell disponibles en HCA?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("2.2.2. Interés en el \"órgano\" immune system, ¿de qué tipos celulares hay datos de single-cell disponibles en HCA?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringImmuneSystemCellType = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?cellType \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasSampleID ?sampleId ;"+
					"    a:SR.hasObjectOfStudy a:ImmuneSystem ;" +
					"    a:SR.hasSelectedCellType ?cellType ." +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringImmuneSystemCellType);
		
		// -----------------------------
		// 2.2.3. ¿Qué tipos celulares son coincidentes entre ambos órganos?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("2.2.3. ¿Qué tipos celulares son coincidentes entre ambos órganos?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringCommonCellType = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?cellType " +
				"WHERE " +
				"{ " +
					"{ " +
						"?id1 rdf:type a:Specimen ;" +
						"     a:SR.hasObjectOfStudy a:Blood ;" +
						"     a:SR.hasSelectedCellType ?cellType ." +
					"} " +
					"{" +
						"?id2 rdf:type a:Specimen ;" +
						"     a:SR.hasObjectOfStudy a:ImmuneSystem ;" +
						"     a:SR.hasSelectedCellType ?cellType ." +
					"}" +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringCommonCellType);
		
		// -----------------------------
		// 2.2.4. ¿Sobre qué enfermedades puedo encontrar datos de single-cell para embrión de Homo Sapiens?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("2.2.4. ¿Sobre qué enfermedades puedo encontrar datos de single-cell para embrión de Homo Sapiens?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringHomoSapiensEmbryoDiseases = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?disease " +
				"WHERE " +
				"{ " +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.belongsToSpecie a:HomoSapiens ;" +
					"    a:SR.hasObjectOfStudy a:Embryo ;" +
					"    a:SR.hasDiseaseStatus ?disease ." +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringHomoSapiensEmbryoDiseases);
		
		// -----------------------------
		// 2.2.5. ¿y Mus Musculus?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("2.2.5. ¿y Mus Musculus?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringMusMusculusEmbryoDiseases = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?disease " +
				"WHERE " +
				"{ " +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.belongsToSpecie a:MusMusculus ;" +
					"    a:SR.hasObjectOfStudy a:Embryo ;" +
					"    a:SR.hasDiseaseStatus ?disease ." +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringMusMusculusEmbryoDiseases);
		
		// -----------------------------
		// 2.2.6. ¿Tenemos datos de single-cell disponibles para un tipo de célula que sea específico de decidua y placenta?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("2.2.6. ¿Tenemos datos de single-cell disponibles para un tipo de célula que sea específico de decidua y placenta?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringCellTypeOnlyDeciduaPlacenta = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?disease " +
				"WHERE " +
				"{ " +
				"{ " +
					"?id1 rdf:type a:Specimen ;" +
					"     a:SR.hasObjectOfStudy a:Decidua ;" +
					"     a:SR.hasSelectedCellType ?cellType ." +
				"} " +
				"{" +
					"?id2 rdf:type a:Specimen ;" +
					"     a:SR.hasObjectOfStudy a:Placenta ;" +
					"     a:SR.hasSelectedCellType ?cellType ." +
				"}" +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringCellTypeOnlyDeciduaPlacenta);
		
		/* 3. Consultas que no podríamos hacer en HCA pero sí en nuestra ontología
		 * 
		 * a) Para demostrar que no arrastramos inconsistencias
		 *	
		 *	En el ejemplo que os mostré en la reunión (está en el pdf que os dejé), veíamos que las partes de órganos descritas para riñón incluían cortex y cortex of kidney, 
		 *  sin embargo, cortex es específico de cerebro. Por lo tanto, la primera consulta que podríamos hacer es que conocer las partes de riñón y cerebro según nuestra 
		 *  ontología.
         *
		 * b) Como usuarios que buscan sobre un tema concreto
		 *  
		 *	¿De cuántos especímenes tendríamos disponibles datos de single-cell cuyo tipo celular pertenezca a la clase leukocytes?
		 *	¿De qué especies tengo datos de single-cell que pertenezcan al reino Plants?
		 * 	¿De cuántos especímenes tenemos disponibles datos de single-cell cuyos donantes (especímenes, indistintamente) tengan la edad expresada en días? ¿De qué SampleType 
		 *  se trata? SI es línea celular, ¿de qué tipo se trata?
		 *	¿De cuántos especímenes disponemos los metadatos, la matriz y los resultados? ¿Cuál son los objectos de estudio?
		 *	¿De qué enfermedades tenemos disponible datos de single-cell donde el "órgano" afectado sea el corazón o, directamente, el sistema circulatorio? ¿Cuáles son estas 
		 *  enfermedades?
		 *	¿Qué proyectos tenemos donde los especímenes estén afectados por una enfermedad clasificada como metabólica y hereditaria? ¿Qué órgano se encuentra afectado? ¿De 
		 *  qué sistema forma parte?
		 */
		

		// -----------------------------
		// 3.1. Demostrar que no arrastramos inconsistencias
		// -----------------------------
		
		// -----------------------------
		// 3.1.1. Partes del riñón
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.1.1. Partes del riñón.");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringKidneyParts = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?kidneyParts " +
				"WHERE " +
				"{ " +
					"?kidneyParts a:OR.isOrganPartOf a:Kidney ;" +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringKidneyParts);
		
		// -----------------------------
		// 3.1.2. Partes del cerebro
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.1.2. Partes del cerebro.");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringBrainParts = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?brainParts " +
				"WHERE " +
				"{ " +
					"?brainParts a:OR.isOrganPartOf a:Brain ;" +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringBrainParts);
		
		// -----------------------------
		// 3.2. Como usuarios
		// -----------------------------
		
		// -----------------------------
		// 3.2.1. ¿De cuántos especímenes tendríamos disponibles datos de single-cell cuyo tipo celular pertenezca a la clase leukocytes?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.1. ¿De cuántos especímenes tendríamos disponibles datos de single-cell cuyo tipo celular pertenezca a la clase leukocytes?.");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringLeukocytesSpecimens = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (COUNT(*) AS ?numSpecimens) " +
				"WHERE " +
				"{ " +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasSelectedCellType ?cellType ." +
					"?cellType rdf:type a:Leukocyte ." +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringLeukocytesSpecimens);
		
		// -----------------------------
		// 3.2.2. ¿De qué especies tengo datos de single-cell que pertenezcan al reino Plants?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.2. ¿De qué especies tengo datos de single-cell que pertenezcan al reino Plants?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringPlantsSpecies = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?plantSpecie " +
				"WHERE " +
				"{ " +
					"?plantSpecie a:OR.belongsToKingdom a:Plants ." +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringPlantsSpecies);
		
		// -----------------------------
		// 3.2.3. ¿De cuántos especímenes tenemos disponibles datos de single-cell cuyos donantes (especímenes, indistintamente) tengan la edad expresada en días?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.3. ¿De cuántos especímenes tenemos disponibles datos de single-cell cuyos donantes (especímenes, indistintamente) tengan la edad expresada en días?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringSpecimensWithAgeInDays = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (COUNT(*) AS ?specimensWithAgeInDays) " +
				"WHERE " +
				"{ " +
					"?id rdf:type a:Specimen ;" +
					"    a:hasAgeUnit ?unit ." +
					"FILTER (?unit = \"d\" || ?unit = \"day\")" +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringSpecimensWithAgeInDays);
		
		
				
		// -----------------------------
		// 3.2.4. ¿De qué SampleType se trata?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.4. ¿De qué SampleType se trata?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringSpecimensWithAgeInDaysSampleType = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?sampleType \n" +
				"WHERE \n" +
				"{ " +
					"?id rdf:type a:Specimen ;" +
					"    a:hasAgeUnit ?unit ;" +
					"    a:SR.hasSampleType ?sampleType ." +
					"FILTER (?unit = \"d\" || ?unit = \"day\") " +
				"}";
		
		// Execute query
		executeQuery(NS, model, queryStringSpecimensWithAgeInDaysSampleType);
		
		// -----------------------------
		// 3.2.5. ¿De cuántos especímenes disponemos los metadatos, la matriz y los resultados?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.5. ¿De cuántos especímenes disponemos los metadatos, la matriz y los resultados?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringSpecimensWith3Types= "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT (COUNT(*) AS ?numSpecimens) \n" +
				"WHERE \n" +
				"{ " +
					"?id rdf:type a:Specimen ;" +
					"    a:hasAvailableDownloadsType \"matrix\" ;" +
					"    a:hasAvailableDownloadsType \"results\" ;" +
					"    a:hasAvailableDownloadsType \"metadata\" ." +
				"}";		
		// Execute query
		executeQuery(NS, model, queryStringSpecimensWith3Types);
		
		// -----------------------------
		// 3.2.6. ¿Cuál son los objetos de estudio?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.6. ¿Cuál son los objetos de estudio?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringObjectsWith3Types= "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?object (COUNT(*) AS ?numSpecimens) \n" +
				"WHERE \n" +
				"{ " +
					"?id rdf:type a:Specimen ;" +
					"    a:hasAvailableDownloadsType \"matrix\" ;" +
					"    a:hasAvailableDownloadsType \"results\" ;" +
					"    a:hasAvailableDownloadsType \"metadata\" ;" +
					"    a:SR.hasObjectOfStudy ?object ." +
				"} " +
				"GROUP BY ?object";		
		// Execute query
		executeQuery(NS, model, queryStringObjectsWith3Types);
		
		// -----------------------------
		// 3.2.7. ¿De qué enfermedades tenemos disponible datos de single-cell donde el "órgano" afectado sea el corazón o, directamente, el sistema circulatorio? ¿Cuáles son estas 
		//        enfermedades?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.7. ¿De qué enfermedades tenemos disponible datos de single-cell donde el \"órgano\" afectado sea el corazón o, directamente, el sistema circulatorio? ¿Cuáles son estas enfermedades?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringDiseaseHeart= "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?diseaseStatus \n" +
				"WHERE \n" +
				"{ " +
					"{ " +
						"?id rdf:type a:Specimen ;" +
						"    a:SR.hasObjectOfStudy a:Heart ;" +
						"    a:SR.hasDiseaseStatus ?diseaseStatus ." +
					"} " +
					"UNION " +
					"{ " +
						"?id rdf:type a:Specimen ;" +
						"    a:SR.hasObjectOfStudy a:CardiovascularSystem ;" +
						"    a:SR.hasDiseaseStatus ?diseaseStatus ." +
					"} " +
				"}";		
		// Execute query
		executeQuery(NS, model, queryStringDiseaseHeart);
		
		// -----------------------------
		// 3.2.8. ¿Qué proyectos tenemos donde los especímenes estén afectados por una enfermedad clasificada como metabólica y hereditaria?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.8. ¿Qué proyectos tenemos donde los especímenes estén afectados por una enfermedad clasificada como metabólica y hereditaria?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringProyectsWithMetabolicOrHereditary= "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?proyect ?diseaseStatus \n" +
				"WHERE \n" +
				"{ " +
					"{ " +
						"?id rdf:type a:Specimen ;" +
						"    a:hasProjectShortName ?proyect ;" +
						"    a:SR.hasDiseaseStatus ?diseaseStatus ." +
						"?diseaseStatus rdf:type a:DiseaseOfMetabolism ." +
					"} " +
					"UNION " +
					"{ " +
						"?id rdf:type a:Specimen ;" +
						"    a:hasProjectShortName ?proyect ;" +
						"    a:SR.hasDiseaseStatus ?diseaseStatus ." +
						"?diseaseStatus rdf:type a:GeneticDisease ." +
					"} " +
				"}";		
		
		// Execute query
		executeQuery(NS, model, queryStringProyectsWithMetabolicOrHereditary);
		
		// -----------------------------
		// 3.2.9. ¿Qué órgano se encuentra afectado?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.9. ¿Qué órgano se encuentra afectado?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringOrgansWithMetabolicOrHereditary = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?diseaseStatus ?object \n" +
				"WHERE \n" +
				"{ " +
					"{ " +
						"?id rdf:type a:Specimen ;" +
						"    a:SR.hasObjectOfStudy ?object ;" +
						"    a:SR.hasDiseaseStatus ?diseaseStatus ." +
						"?diseaseStatus rdf:type a:DiseaseOfMetabolism ." +
						"?object rdf:type a:Organ ." +
					"} " +
					"UNION " +
					"{ " +
						"?id rdf:type a:Specimen ;" +
						"    a:SR.hasObjectOfStudy ?object ;" +
						"    a:SR.hasDiseaseStatus ?diseaseStatus ." +
						"?diseaseStatus rdf:type a:GeneticDisease ." +
						"?object rdf:type a:Organ ." +
					"} " +
				"}";		
		
		// Execute query
		executeQuery(NS, model, queryStringOrgansWithMetabolicOrHereditary);
		
		// -----------------------------
		// 3.2.10. ¿De qué sistema forma parte?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.10. ¿De qué sistema forma parte?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringSystemsWithMetabolicOrHereditary = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT DISTINCT ?diseaseStatus ?object ?system \n" +
				"WHERE \n" +
				"{ " +
					"{ " +
						"?id rdf:type a:Specimen ;" +
						"    a:SR.hasObjectOfStudy ?object ;" +
						"    a:SR.hasDiseaseStatus ?diseaseStatus ." +
						"?diseaseStatus rdf:type a:DiseaseOfMetabolism ." +
						"?object rdf:type a:Organ ;" +
						"        a:OR.isPartOfSystem ?system ." +
					"} " +
					"UNION " +
					"{ " +
						"?id rdf:type a:Specimen ;" +
						"    a:SR.hasObjectOfStudy ?object ;" +
						"    a:SR.hasDiseaseStatus ?diseaseStatus ." +
						"?diseaseStatus rdf:type a:GeneticDisease ." +
						"?object rdf:type a:Organ ;" +
						"        a:OR.isPartOfSystem ?system ." +
					"} " +
				"}";		
		
		// Execute query
		executeQuery(NS, model, queryStringSystemsWithMetabolicOrHereditary);
		
		// -----------------------------
		// 3.2.11. ¿Cuál es el laboratorio que más proyectos tiene y cuál es su principal órgano estudiado?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.11. ¿Cuál es el laboratorio que más proyectos tiene y cuál es su principal órgano estudiado?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringMaxLab = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?lab (COUNT(DISTINCT ?project) as ?numberOfProyects) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasLaboratory ?lab ;" +
					"    a:hasProjectTitle ?project ." +
				"}" +
				"GROUP BY ?lab \n" +
				"ORDER BY DESC(?numberOfProyects) \n" +
				"LIMIT 1";
		
		// Execute query
		executeQuery(NS, model, queryStringMaxLab);
		
		String queryStringMaxLabOrgan = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?organ (COUNT(*) as ?numberOfOccurrences) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:hasLaboratory \"HumanCellAtlasDataCoordinationPlatform\" ;" +
					"    a:SR.hasObjectOfStudy ?organ ." +
				"}" +
				"GROUP BY ?organ \n" +
				"ORDER BY DESC(?numberOfOccurrences) \n" +
				"LIMIT 1";
		
		// Execute query
		executeQuery(NS, model, queryStringMaxLabOrgan);
		
		// -----------------------------
		// 3.2.12. ¿Cuál es el órgano para el cual tenemos un mayor número de enfermedades estudiadas?
		// -----------------------------
		System.out.println();
		System.out.println("------------------------");
		System.out.println("3.2.12. ¿Cuál es el órgano para el cual tenemos un mayor número de enfermedades estudiadas?");
		System.out.println("------------------------");
		System.out.println();
		
		String queryStringDiseasesPerOrgan = "PREFIX a: <" + NS + "> " +
				"PREFIX rdf: <" + rdf + "> " +
				"PREFIX xsd: <" + xsd + "> " +
				"SELECT ?organ (COUNT( DISTINCT ?disease ) as ?numberOfDiseases) \n" +
				"WHERE" +
				"{" +
					"?id rdf:type a:Specimen ;" +
					"    a:SR.hasObjectOfStudy ?organ ;" +
					"    a:SR.hasDiseaseStatus ?disease ." +
				"}" +
				"GROUP BY ?organ \n" +
				"ORDER BY DESC(?numberOfDiseases) \n" +
				"LIMIT 1";
		
		// Execute query
		executeQuery(NS, model, queryStringDiseasesPerOrgan);
	}

}
