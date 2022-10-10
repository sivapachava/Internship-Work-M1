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

Switch = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/vl10/B17")
g.add((Switch, rdf.type, pto.Proximity_sensor))
g.add((Switch, rdf.type, eco.C_AGZ376003))
g.add((Switch, rdf.type, sosa.sensor))
g.add((Switch, rdfs.label, Literal("Miniature photo-electric proximity sensor")))
g.add((Switch, skos.prefLabel, Literal("B17")))
g.add((Switch, rdfs.comment, Literal("Proximity Sensor sensed the presence of nearby objects without any physical contact with the objects", lang=("en"))))
g.add((Switch, sosa.observes, Literal("It indicates presence of bottle at end of the conveyor belt on the VL10 of the IT'm factory.", lang=("en"))))
g.add((Switch, schema.manufacture, Literal("SICK Sensor Intelligence")))
g.add((Switch, dct.identifier,Literal("https://shop.appliedc.com/products/1042049")))
g.add((Switch, td.hasPropertyAffordance, machine))
g.add((machine, rdf.type, td.PropertyAffordance))
g.add((machine, rdf.type, js.BooleanSchema))
g.add((machine, rdf.type, onto.OpticalSensorStatus))
g.add((machine, dct.title, Literal("conveyor down status")))
g.add((machine, dct.description, Literal("Indicates the bottle is present at the end/down position of the conveyor belt on the VL10 Machine of the IT'm factory.(downstream presence).", lang=("en"))))
g.add((machine, js.readOnly, Literal("True")))
g.add((machine, js.writeOnly, Literal("False")))
g.add((machine, td.hasForm, Operation))             
g.add((Operation, rdf.type, hctl.Form))
g.add((Operation, htv.methodName, Literal("GET")))
g.add((Operation, hctl.forContentType, Literal("application/json")))
g.add((Operation, hctl.hasOperationType, td.readProperty))
g.add((Operation, hctl.hasTarget, Literal("http://localhost:3001/ns=2;s=Channel_test2.Magasin%20vertical.Accumulation_Aval")))
g.add((machine, td.isObservable, Literal("False")))
g.add((machine, td.name, Literal("Accumulation_Aval")))

print(g.serialize(r"C:\Users\Siva Ratnam Pachava\OneDrive\Desktop\InternshipM1\VL10\B17.ttl", format='turtle'))