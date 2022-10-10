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

Switch = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/xy10/B19")
g.add((Switch, rdf.type, pto.Proximity_sensor))
g.add((Switch, rdf.type, eco.C_AGZ376003))
g.add((Switch, rdf.type, sosa.Sensor))
g.add((Switch, skos.prefLabel, Literal("B19")))
g.add((Switch, rdfs.Label, Literal("E proximity Switch type Sensor")))
g.add((Switch, rdfs.comment, Literal("Proximity Sensor sensed the presence of nearby objects without any physical contact with the objects", lang=("en"))))
g.add((Switch, sosa.observes, Literal("It indicates belt reaches to bottom limit point on the Z Axis on XY10 machine of the IT'm factory", lang=("en"))))
g.add((Switch, schema.manufacturer, Literal("igus")))
g.add((Switch, dct.identifier, Literal("https://www.igus.com/product?artNr=INI-AB-I-025-B-AA")))
g.add((Switch, td.hasPropertyAffordance, machine))
g.add((machine, rdf.type, td.PropertyAffordance))
g.add((machine, rdf.type, js.BooleanSchema))
g.add((machine, dct.title, Literal("ZAxis bottom Limit")))
g.add((machine, dct.description, Literal("Indicates the status of the Z axis on XY10 machine of the IT'm factory at the bottom limit point. Normally the switch is in close and the status is true, if belt reaches to bottom limit point then the switch is opened and the status is false.", lang=("en"))))
g.add((machine, js.readOnly, Literal("True")))
g.add((machine, js.writeOnly, Literal("False")))
g.add((machine, td.hasForm, Operation))             
g.add((Operation, rdf.type, hctl.Form))
g.add((Operation, htv.methodName, Literal("GET")))
g.add((Operation, hctl.forContentType, Literal("application/json")))
g.add((Operation, hctl.hasOperationType, td.readProperty))
g.add((Operation, hctl.hasTarget, Literal("https://ci.mines-stetienne.fr/simu/packagingWorkshop/properties/AxeZ_Fdc_Bas_B19")))
g.add((machine, td.isObservable, Literal("False")))
g.add((machine, td.name, Literal("AxeZ_Fdc_Bas_B19")))

print(g.serialize(r"C:\Users\Siva Ratnam Pachava\OneDrive\Desktop\InternshipM1\XY10\B19.ttl" , format='ttl'))