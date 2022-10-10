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


Switch = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/xy10/B14")
g.add((Switch, rdf.type, pto.Vacuum_pump))
g.add((Switch, rdf.type, eco.C_AKL924002))
g.add((Switch, rdfs.label, Literal("Vacuum Unit - Ejector System/ Vacuum Pump System", lang=("en"))))
g.add((Switch,  skos.prefLabel, Literal("B14")))
g.add((Switch, rdfs.comment, Literal("vaccum unit is used to change the pressure in a contained space to create a motion", lang=("en"))))
g.add((Switch, schema.manufacture, Literal("SMC")))
g.add((Switch, dct.identifier, Literal("https://www.smc.eu/en-eu/products/zk2-a~164877~nav?productId=164879")))
g.add((Switch, td.hasPropertyAffordance, machine))
g.add((machine, rdf.type, td.PropertyAffordance))
g.add((machine, rdf.type, js.BooleanSchema))
g.add((machine, dct.title, Literal("Vaccum switch1 Reference")))
g.add((machine, dct.description, Literal("Indicates the belt is reaches to the intial position on the Z axis on XY10 machine of the IT'm factory. Normally the switch is in open and the status is false, if belt reaches to intial position then the switch is closed and the status is true.", lang=("en"))))
g.add((machine, js.readOnly, Literal("True")))
g.add((machine, js.writeOnly, Literal("False")))
g.add((machine, td.hasForm, Operation))             
g.add((Operation, rdf.type, hctl.Form))
g.add((Operation, htv.methodName, Literal("GET")))
g.add((Operation, hctl.forContentType, Literal("application/json")))
g.add((Operation, hctl.hasOperationType, td.readProperty))
g.add((Operation, hctl.hasTarget, Literal("https://ci.mines-stetienne.fr/simu/packagingWorkshop/properties/Vacu_Prise_Prod1_B14_1")))
g.add((machine, td.isObservable, Literal("False")))
g.add((machine, td.name, Literal("Vacu_Prise_Prod1_B14_1")))

print(g.serialize(r"C:\Users\Siva Ratnam Pachava\OneDrive\Desktop\InternshipM1\XY10\B14.ttl", format='turtle'))