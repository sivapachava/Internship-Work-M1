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

Motor = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/xy10/M1")
g.add((Motor, rdf.type, pto.motor))
g.add((Motor, rdf.type, eco.C_AKE175002))
g.add((Motor, rdfs.label, Literal("Gear Motor", lang=("en"))))
g.add((Motor,  skos.prefLabel, Literal("M1")))
g.add((Motor, rdfs.comment, Literal("Gear motor for conveyor belt on the XY10 of the IT'm factory", lang=("en"))))
g.add((Motor, schema.manufacture, Literal("TRANSTECNO")))
g.add((Motor, dct.identifier, Literal("https://www.maxodeals.com/mdenglish/transtecno-tcm030-0220-ttn-ts6324b14-used-ump")))
g.add((Motor, td.hasPropertyAffordance, machine))
g.add((machine, rdf.type, td.PropertyAffordance))
g.add((machine, rdf.type, js.NumberSchema))
g.add((machine, rdf.type, onto.ConveyorSpeed))
g.add((machine, dct.title, Literal("Conveyor Speed")))
g.add((machine, dct.description, Literal("It is used to read and write the speed of the conveyor belt on the XY10 Machine of the IT'm factory.", lang=("en"))))
g.add((machine, js.readOnly, Literal("False")))
g.add((machine, js.writeOnly, Literal("False")))
g.add((machine, td.hasForm, Operation))             
g.add((Operation, rdf.type, hctl.Form))
g.add((Operation, htv.methodName, Literal("GET")))
g.add((Operation, hctl.forContentType, Literal("application/json")))
g.add((Operation, hctl.hasOperationType, td.readProperty))
g.add((Operation, hctl.hasOperationType, td.writeProperty))
g.add((Operation, hctl.hasTarget, Literal("https://ci.mines-stetienne.fr/simu/storageRack/properties/ConsigneVitesseConvoyeur")))
g.add((machine, td.isObservable, Literal("False")))
g.add((machine, td.name, Literal("ConsigneVitesseConvoyeur")))

print(g.serialize(r"C:\Users\Siva Ratnam Pachava\OneDrive\Desktop\InternshipM1\XY10\M1.ttl" , format='turtle'))