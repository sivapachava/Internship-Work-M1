import csv
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
                 
with open('./XY10 Labels.csv', 'r') as file:
    csvreader = csv.reader(file)  
    for row in csvreader:
        g = Graph()
        machine = BNode()
        Operation = BNode()
        gg = Literal("GET")
        appjs = Literal("application/json")       

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
        
        print(row)
        type = pto[row[1]]
        type1 = pto[row[2]]
        id = eco[row[3]]
        design = Literal(row[4])
        ref = Literal(row[5])
        label = Literal(row[6], lang=("en"))
        descr = Literal(row[7], lang=("en"))
        purps = URIRef(row[8])
        bool = js[row[9]]
        title = Literal(row[10])
        moreinfo = Literal(row[11])
        trst = Literal(row[12], datatype = XSD.boolean)
        frst = Literal(row[13], datatype = XSD.boolean)
        target = URIRef(row[14])
        frst1 = Literal(row[15], datatype = XSD.boolean)
        nnaammee = Literal(row[16])
        wrt = td[row[17]]
        
        
        Sensor = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/xy10" + "/" + row[0])
        g.add((Sensor, rdf.type, type))
        g.add((Sensor, rdf.type, type1))
        g.add((Sensor, rdf.type, id))
        g.add((Sensor, schema.manufacturer, design))
        g.add((Sensor, dct.identifier, ref))
        g.add((Sensor, rdfs.label, label))
        g.add((Sensor, rdfs.comment, descr))
        g.add((Sensor, sosa.observes, purps))
        g.add((Sensor, td.hasPropertyAffordance, machine))
        g.add((machine, rdf.type, td.PropertyAffordance))
        g.add((machine, rdf.type, bool))
        g.add((machine, dct.title, title))
        g.add((machine, dct.description, moreinfo))
        g.add((machine, js.readOnly, trst))
        g.add((machine, js.writeOnly, frst))
        g.add((machine, td.hasForm, Operation))
        g.add((Operation, rdf.type, hctl.Form))
        g.add((Operation, htv.methodName, gg))
        g.add((Operation, hctl.forContentType, appjs))
        g.add((Operation, hctl.hasOperationType, td.readProperty))
        g.add((Operation, hctl.hasOperationType, wrt)) 
        g.add((Operation, hctl.hasTarget, target))
        g.add((machine, td.isObservable, frst1))
        g.add((machine, td.name, nnaammee))
        
        
        print(g.serialize(r"C:\Users\Siva Ratnam Pachava\OneDrive\Desktop\InternshipM1\CSV Files and related PY Files\XY10 Labels turtle files" + "/" + row[0] + ".ttl" , format="ttl"))

    file.close()
    