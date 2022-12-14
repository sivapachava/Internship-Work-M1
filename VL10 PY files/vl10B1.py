from rdflib import Graph, Namespace, URIRef, Literal, BNode, XSD

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
truest = Literal("true", datatype = XSD.boolean)
falsest = Literal("false", datatype = XSD.boolean)
b1obs = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/vl10/B1#this")
b1target = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/vl10/B1#AxeX_Fdc_Arriere_B1")

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

Switch = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/vl10/B1")
g.add((Switch, rdf.type, pto.Proximity_sensor))
g.add((Switch, rdf.type, eco.C_AGZ376003))
g.add((Switch, rdf.type, sosa.Sensor))
g.add((Switch, skos.prefLabel, Literal("B1")))
g.add((Switch, rdfs.label, Literal("E proximity Switch type Sensor")))
g.add((Switch, rdfs.comment, Literal("It indicates the Cartesian robot belt reaches to end limit point on the X- Axis on VL10 machine of the IT'm factory.", lang=("en"))))
g.add((Switch, schema.manufacturer, Literal("igus")))
g.add((Switch, dct.identifier, Literal("https://www.igus.com/product?artNr=INI-AB-I-025-B-AA")))
g.add((Switch, sosa.observes, b1obs))
g.add((Switch, td.hasPropertyAffordance, machine))
g.add((machine, rdf.type, td.PropertyAffordance))
g.add((machine, rdf.type, js.BooleanSchema))
g.add((machine, dct.title, Literal("AxeX_Fdc_Arriere_B1")))
g.add((machine, dct.description, Literal("Indicates the status of the Cartesian robot X axis at the end limit point on VL10 machine of the IT'm factory. Normally the switch is in close and the status is true, if the Cartesian robot belt reaches to end point then the switch is opened and the status is false.", lang=("en"))))
g.add((machine, js.readOnly, truest))
g.add((machine, js.writeOnly, falsest))
g.add((machine, td.hasForm, Operation))             
g.add((Operation, rdf.type, hctl.Form))
g.add((Operation, htv.methodName, Literal("GET")))
g.add((Operation, hctl.forContentType, Literal("application/json")))
g.add((Operation, hctl.hasOperationType, td.readProperty))
g.add((Operation, hctl.hasTarget, b1target))
g.add((machine, td.isObservable, falsest))
g.add((machine, td.name, Literal("AxeX_Fdc_Arriere_B1")))

print(g.serialize(r"C:\Users\Siva Ratnam Pachava\OneDrive\Desktop\InternshipM1\VL10\B1.ttl" , format='ttl'))