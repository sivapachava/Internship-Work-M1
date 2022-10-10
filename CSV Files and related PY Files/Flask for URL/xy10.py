import csv
from rdflib import Graph, Namespace, URIRef, Literal, BNode,XSD
from flask import Flask

app = Flask(__name__)
@app.route('/xy10', methods = ['GET'])

def xy10B1():
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    schema1 = Namespace("http://schema.org/")
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
    wotsec = Namespace("https://www.w3.org/2019/wot/security#")

    g = Graph()

    g.bind("rdf", rdf)
    g.bind("rdfs", rdfs)
    g.bind("schema", schema1)
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
    g.bind("wotsec", wotsec)


    machine1 = BNode()
    Operation1 = BNode()
    last = BNode()
    gg = Literal("GET")
    appjs = Literal("application/json")
    descrmach = Literal("XY10 packaging workshop")
    stopbutntarget = URIRef("http://localhost:3001/ns=2;s=ITm%20Factory.XY10.pressEmergencyStop")
    Sensor = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/xy10/fullgraph")

    g.add((Sensor, rdf.type, td.thing))
    g.add((Sensor, rdf.type, sosa.Platform))
    g.add((Sensor, rdf.type,  pto.Packaging_machinery))
    g.add((Sensor, rdfs.label, Literal("Cartesian robot XYZ", lang = ("en"))))
    g.add((Sensor, dct.title, Literal("packagingWorkshop")))
    g.add((Sensor, dct.description, descrmach))
    g.add((Sensor, rdfs.comment, Literal("Brushless axis dosing machine", lang = ("en"))))
    g.add((Sensor, td.hasActionAffordance, machine1))
    g.add((machine1, rdf.type, td.ActionAffordance))
    g.add((machine1, rdf.type, onto.StopInEmergencyAction))
    g.add((machine1, dct.title, Literal("Press Emergency Stop")))
    g.add((machine1, dct.description,Literal("turns off all active components of the machine")))
    g.add((machine1, td.hasForm, Operation1))
    g.add((Operation1, rdf.type, hctl.Form))
    g.add((Operation1, htv.methodName, Literal("POST")))
    g.add((Operation1, hctl.forContentType, appjs))
    g.add((Operation1, hctl.hasOperationType, td.invokeAction))
    g.add((Operation1, hctl.hasTarget, stopbutntarget))
    g.add((machine1, td.isIdempotent, Literal("false", datatype = XSD.boolean)))
    g.add((machine1, td.isSafe, Literal("false", datatype = XSD.boolean)))
    g.add((machine1, td.name, Literal("I0.0")))
    g.add((Sensor, td.hasSecurityConfiguration, last))
    g.add((last, rdf.type, wotsec.BasicSecurityScheme)) 


    with open("C:\\Users\\Siva Ratnam Pachava\\OneDrive\\Desktop\\InternshipM1\\CSV Files and related PY Files\\XY10 thing desc file.csv", 'r') as file:
        csvreader = csv.reader(file)  
        for row in csvreader:
            machine = BNode()
            Operation = BNode()
            
            wrt = js[row[1]]
            title = Literal(row[2])
            moreinfo = Literal(row[3])
            trst = Literal(row[4], datatype = XSD.boolean)
            frst = Literal(row[5], datatype = XSD.boolean)
            target = URIRef(row[6])
            frst1 = Literal(row[7], datatype = XSD.boolean)
            nnaammee = Literal(row[8])
            extrprt = td[row[9]]
            
            
            g.add((Sensor, td.hasPropertyAffordance, machine))
            g.add((machine, rdf.type, td.PropertyAffordance))
            g.add((machine, rdf.type, wrt))
            g.add((machine, dct.title, title))
            g.add((machine, dct.description, moreinfo))
            g.add((machine, js.readOnly, trst))
            g.add((machine, js.writeOnly, frst))
            g.add((machine, td.hasForm, Operation))
            g.add((Operation, rdf.type, hctl.Form))
            g.add((Operation, htv.methodName, gg))
            g.add((Operation, hctl.forContentType, appjs))
            g.add((Operation, hctl.hasOperationType, td.readProperty))
            g.add((Operation, hctl.hasOperationType, extrprt))
            g.add((Operation, hctl.hasTarget, target))
            g.add((machine, td.isObservable, frst1))
            g.add((machine, td.name, nnaammee))
            
            print(row)
        file.close()
    return(g.serialize(format = "turtle"))
if __name__ == "__main__":
    app.run(debug=True)