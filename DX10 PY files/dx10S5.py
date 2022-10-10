from rdflib import Graph, Namespace, URIRef, Literal,BNode

rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
schema = Namespace("http://schema.org/")
pto = Namespace("http://www.productontology.org/id/")
dct = Namespace("http://purl.org/dc/terms/")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")
eco = Namespace("http://www.ebusiness-unibw.org/ontologies/eclass/5.1.4#")
sosa = Namespace("http://www.w3.org/ns/sosa/")
td = Namespace("https://www.w3.org/2019/wot/td#")
onto = Namespace("https://ci.mines-stetienne.fr/kg/ontology#")
hctl = Namespace("https://www.w3.org/2019/wot/hypermedia#")
htv = Namespace("http://www.w3.org/2011/http#")                 
js = Namespace("https://www.w3.org/2019/wot/json-schema#")            
                 
g = Graph()
machine = BNode()
Operation = BNode()

g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("schema", schema)
g.bind("pto", pto)
g.bind("dct", dct)
g.bind("skos", skos)
g.bind("eco", eco)
g.bind("sosa", sosa)
g.bind("td", td)
g.bind("onto", onto)
g.bind("hctl", hctl)
g.bind("htv", htv)
g.bind("js", js)

Cylinder = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/dx10/S5")
g.add((Cylinder, rdf.type, pto.Switch))
g.add((Cylinder, rdf.type, eco.C_AAC028004))
g.add((Cylinder, rdfs.Label, Literal("Enclosed Switch")))
g.add((Cylinder, skos.prefLabel, Literal("S5")))
g.add((Cylinder, rdfs.comment, Literal("Used to stop movable objects", lang=("en"))))
g.add((Cylinder, schema.manufacture, Literal("OMRON industrial automation")))
g.add((Cylinder, sosa.observes,  Literal("Indicates movable part (hopper) reaches to end position on forward direction on DX10 machine of the IT'm factory.", lang=("en"))))
g.add((Cylinder, dct.identifier, Literal("https://www.ia.omron.com/product/item/11177/")))
g.add((Cylinder, td.hasPropertyAffordance, machine))
g.add((machine, rdf.type, td.PropertyAffordance))
g.add((machine, rdf.type, js.BooleanSchema))
g.add((machine, dct.title, Literal("Axe_Remplissage_Sens")))
g.add((machine, dct.description, Literal("Indicates tank reaches to ideal/intial position on forward direction on DX10 machine of the IT'm factory.", lang=("en"))))
g.add((machine, js.readOnly, Literal("True")))
g.add((machine, js.writeOnly, Literal("False")))
g.add((machine, td.hasForm, Operation))             
g.add((Operation, rdf.type, hctl.Form))
g.add((Operation, htv.methodName, Literal("GET")))
g.add((Operation, hctl.forContentType, Literal("application/json")))
g.add((Operation, hctl.hasOperationType, td.readProperty))
g.add((Operation, hctl.hasTarget, Literal("https://ci.mines-stetienne.fr/simu/fillingWorkshop/properties/Axe_Remplissage_Sens")))
g.add((machine, td.isObservable, Literal("False")))
g.add((machine, td.name, Literal("Axe_Remplissage_Sens")))

print(g.serialize(r"C:\Users\Siva Ratnam Pachava\OneDrive\Desktop\InternshipM1\DX10\S5.ttl", format='turtle'))