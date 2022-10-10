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

Motor = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/vl10/M4")
g.add((Motor, rdf.type, pto.Stepper_motor))
g.add((Motor, rdf.type, eco.C_AKE143002))
g.add((Motor, rdfs.label, Literal("E stepper motor with encoder", lang=("en"))))
g.add((Motor,  skos.prefLabel, Literal("M4")))
g.add((Motor, rdfs.comment, Literal("Stepper motor for X-Axis moving on the VL10 of the IT'm factory", lang=("en"))))
g.add((Motor, schema.manufacture, Literal("IGUS")))
g.add((Motor, dct.identifier, Literal("https://www.igus.com/product?artNr=MOT-AN-S-060-020-056-M-C-AAAC")))
g.add((Motor, td.hasPropertyAffordance, machine))
g.add((machine, rdf.type, td.PropertyAffordance))
g.add((machine, rdf.type, js.IntegerSchema))
g.add((machine, rdf.type, onto.XCoordinate))
g.add((machine, dct.title, Literal("Position Z")))
g.add((machine, dct.description, Literal("It is used to read the position of the cartesian motor on Z-Axis", lang=("en"))))
g.add((machine, js.readOnly, Literal("True")))
g.add((machine, js.writeOnly, Literal("False")))
g.add((machine, td.hasForm, Operation))             
g.add((Operation, rdf.type, hctl.Form))
g.add((Operation, htv.methodName, Literal("GET")))
g.add((Operation, hctl.forContentType, Literal("application/json")))
g.add((Operation, hctl.hasOperationType, td.readProperty))
g.add((Operation, hctl.hasTarget, Literal("http://localhost:3001/ns=2;s=Channel_test2.Magasin%20vertical.Vitesse_Deplacement_Z")))
g.add((machine, td.isObservable, Literal("False")))
g.add((machine, td.name, Literal("Vitesse_Deplacement_Z")))

print(g.serialize(r"C:\Users\Siva Ratnam Pachava\OneDrive\Desktop\InternshipM1\VL10\M4.ttl" , format='turtle'))