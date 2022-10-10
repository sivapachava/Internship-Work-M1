from rdflib import Graph, Namespace, URIRef, Literal, BNode, XSD

rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
dct = Namespace("http://purl.org/dc/terms/")
sosa = Namespace("http://www.w3.org/ns/sosa/")
td = Namespace("https://www.w3.org/2019/wot/td#")
onto = Namespace("https://ci.mines-stetienne.fr/kg/ontology#")
hctl = Namespace("https://www.w3.org/2019/wot/hypermedia#")
htv = Namespace("http://www.w3.org/2011/http#")                 
js = Namespace("https://www.w3.org/2019/wot/json-schema#")

g = Graph()

machine = BNode()
machine1 = BNode()
machine2 = BNode()
machine3 = BNode()
machine4 = BNode()
machine5 = BNode()
machine6 = BNode()
machine7 = BNode()

Operation = BNode()
Operation1 = BNode()
Operation2 = BNode()
Operation3 = BNode()
Operation4 = BNode()
Operation5 = BNode()
Operation6 = BNode()
Operation7 = BNode()

truest = Literal("true", datatype = XSD.boolean)
falsest = Literal("false", datatype = XSD.boolean)

g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("dct", dct)
g.bind("sosa", sosa)
g.bind("td", td)
g.bind("onto", onto)
g.bind("hctl", hctl)
g.bind("htv", htv)
g.bind("js", js)

b1target = URIRef("http://localhost:3001/ns=2;s=Channel_test2.Magasin%20vertical.AxeX_Fdc_Arriere_B1")
b6target = URIRef("http://localhost:3001/ns=2;s=Channel_test2.Magasin%20vertical.AxeZ_Ref")
b7target = URIRef("http://localhost:3001/ns=2;s=Channel_test2.Magasin%20vertical.Verin_Sas_Rentree")
b14target = URIRef("http://localhost:3001/ns=2;s=Channel_test2.Magasin%20vertical.Ouverture_Pinces")
b17target = URIRef("http://localhost:3001/ns=2;s=Channel_test2.Magasin%20vertical.Accumulation_Aval")
m1target = URIRef("http://localhost:3001/ns=2;s=Channel_test2.Magasin%20vertical.Consigne%20vitesse%20convoyeur")
m2target = URIRef("http://localhost:3001/ns=2;s=Channel_test2.Magasin%20vertical.Vitesse_Deplacement_X")
m4target = URIRef("http://localhost:3001/ns=2;s=Channel_test2.Magasin%20vertical.Vitesse_Deplacement_Z")

tr = URIRef("https://ci.mines-stetienne.fr/simu/storageRack")

Workshop = URIRef("https://ci.mines-stetienne.fr/kg/itmfactory/vl10/sample")
g.add((Workshop, rdf.type, td.thing))
g.add((Workshop, rdf.type, sosa.Platform))
g.add((Workshop, rdfs.label, Literal("vertical dynamic storage rack", lang=("en"))))
g.add((Workshop, rdfs.comment, Literal("VL10 storage rack with a Cartesian robot and a conveyor belt. It can be used as a conveying workshop: The Cartesian robot can be used to move on the XZ-plane, pick up items from the storage rack and place them on the one end of the conveyor belt.", lang=("en"))))
g.add((Workshop, dct.title, Literal("VL10")))
g.add((Workshop, onto.hasThingDescription, tr))
g.add((Workshop, td.hasPropertyAffordance, machine))
g.add((machine, rdf.type, td.PropertyAffordance))
g.add((machine, rdf.type, js.BooleanSchema))
g.add((machine, dct.title, Literal("X Axis end limit status")))
g.add((machine, dct.description, Literal("Indicates the status of the X axis at the end point on VL10 machine of the IT'm factory. Normally the switch is in close and the status is true, if belt reaches to end point then the switch is opened and the status is false.", lang=("en"))))
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


g.add((Workshop, td.hasPropertyAffordance, machine1))
g.add((machine1, rdf.type, onto.ZCoordinate))
g.add((machine1, rdf.type, onto.OpticalSensorStatus))
g.add((machine1, rdf.type, td.PropertyAffordance))
g.add((machine1, rdf.type, js.BooleanSchema))
g.add((machine1, dct.title, Literal("Z-Axis reference Status")))
g.add((machine1, dct.description, Literal("Indicates the status of the Z axis reference on VL10 machine of the IT'm factory. Normally the switch is in open and the status is false, if belt reaches to intial/ideal position on the Z-Axis then the switch is closed and the status is true.", lang=("en"))))
g.add((machine1, js.readOnly, truest))
g.add((machine1, js.writeOnly, falsest))
g.add((machine1, td.hasForm, Operation1))             
g.add((Operation1, rdf.type, hctl.Form))
g.add((Operation1, htv.methodName, Literal("GET")))
g.add((Operation1, hctl.forContentType, Literal("application/json")))
g.add((Operation1, hctl.hasOperationType, td.readProperty))
g.add((Operation1, hctl.hasTarget, b6target))
g.add((machine1, td.isObservable, falsest))
g.add((machine1, td.name, Literal("AxeZ_Ref")))


g.add((Workshop, td.hasPropertyAffordance, machine2))
g.add((machine2, rdf.type, td.PropertyAffordance))
g.add((machine2, rdf.type, js.BooleanSchema))
g.add((machine2, dct.title, Literal("Air lock cylinder status")))
g.add((machine2, dct.description, Literal("Indicates the bottle is present at the airlock cylinder on the conveyor belt on VL10 machine of the IT'm factory. Normally the air lock is in off and the status is true, if the bottle reaches to airlock place and at that time one more bottle is present at the downstream of the conveyor then air lock is on and the status is false.", lang=("en"))))
g.add((machine2, js.readOnly, truest))
g.add((machine2, js.writeOnly, falsest))
g.add((machine2, td.hasForm, Operation2))             
g.add((Operation2, rdf.type, hctl.Form))
g.add((Operation2, htv.methodName, Literal("GET")))
g.add((Operation2, hctl.forContentType, Literal("application/json")))
g.add((Operation2, hctl.hasOperationType, td.readProperty))
g.add((Operation2, hctl.hasTarget, b7target))
g.add((machine2, td.isObservable, falsest))
g.add((machine2, td.name, Literal("Verin_Sas_Rentree")))



g.add((Workshop, td.hasPropertyAffordance, machine3))
g.add((machine3, rdf.type, td.PropertyAffordance))
g.add((machine3, rdf.type, js.BooleanSchema))
g.add((machine3, dct.title, Literal("Y Axis airlock cylinder status")))
g.add((machine3, dct.description, Literal("Indicates the status/condiation/position of the Y Axis airlock cylinder on the VL10 Machine of the IT'm factory.", lang=("en"))))
g.add((machine3, js.readOnly, truest))
g.add((machine3, js.writeOnly, falsest))
g.add((machine3, td.hasForm, Operation3))             
g.add((Operation3, rdf.type, hctl.Form))
g.add((Operation3, htv.methodName, Literal("GET")))
g.add((Operation3, hctl.forContentType, Literal("application/json")))
g.add((Operation3, hctl.hasOperationType, td.readProperty))
g.add((Operation3, hctl.hasTarget, b14target))
g.add((machine3, td.isObservable, falsest))
g.add((machine3, td.name, Literal("Ouverture_Pinces")))



g.add((Workshop, td.hasPropertyAffordance, machine4))
g.add((machine4, rdf.type, td.PropertyAffordance))
g.add((machine4, rdf.type, js.BooleanSchema))
g.add((machine4, rdf.type, onto.OpticalSensorStatus))
g.add((machine4, dct.title, Literal("conveyor down status")))
g.add((machine4, dct.description, Literal("Indicates the bottle is present at the end/down position of the conveyor belt on the VL10 Machine of the IT'm factory.(downstream presence).", lang=("en"))))
g.add((machine4, js.readOnly, truest))
g.add((machine4, js.writeOnly, falsest))
g.add((machine4, td.hasForm, Operation4))             
g.add((Operation4, rdf.type, hctl.Form))
g.add((Operation4, htv.methodName, Literal("GET")))
g.add((Operation4, hctl.forContentType, Literal("application/json")))
g.add((Operation4, hctl.hasOperationType, td.readProperty))
g.add((Operation4, hctl.hasTarget, b17target))
g.add((machine4, td.isObservable, falsest))
g.add((machine4, td.name, Literal("Accumulation_Aval")))



g.add((Workshop, td.hasPropertyAffordance, machine5))
g.add((machine5, rdf.type, td.PropertyAffordance))
g.add((machine5, rdf.type, js.NumberSchema))
g.add((machine5, rdf.type, onto.ConveyorSpeed))
g.add((machine5, dct.title, Literal("Conveyor Speed")))
g.add((machine5, dct.description, Literal("It is used to read and write the speed of the conveyor belt on the VL10 Machine of the IT'm factory.", lang=("en"))))
g.add((machine5, js.readOnly, falsest))
g.add((machine5, js.writeOnly, falsest))
g.add((machine5, td.hasForm, Operation5))             
g.add((Operation5, rdf.type, hctl.Form))
g.add((Operation5, htv.methodName, Literal("GET")))
g.add((Operation5, hctl.forContentType, Literal("application/json")))
g.add((Operation5, hctl.hasOperationType, td.readProperty))
g.add((Operation5, hctl.hasOperationType, td.writeProperty))
g.add((Operation5, hctl.hasTarget, Literal("http://localhost:3001/ns=2;s=Channel_test2.Magasin%20vertical.Consigne%20vitesse%20convoyeur")))
g.add((machine5, td.isObservable, falsest))
g.add((machine5, td.name, Literal("Consigne vitesse convoyeur")))


g.add((Workshop, td.hasPropertyAffordance, machine6))
g.add((machine6, rdf.type, td.PropertyAffordance))
g.add((machine6, rdf.type, js.IntegerSchema))
g.add((machine6, rdf.type, onto.XCoordinate))
g.add((machine6, dct.title, Literal("Position X")))
g.add((machine6, dct.description, Literal("It is used to read the speed of the cartesian motor on X-Axis", lang=("en"))))
g.add((machine6, js.readOnly, falsest))
g.add((machine6, js.writeOnly, falsest))
g.add((machine6, td.hasForm, Operation6))             
g.add((Operation6, rdf.type, hctl.Form))
g.add((Operation6, htv.methodName, Literal("GET")))
g.add((Operation6, hctl.forContentType, Literal("application/json")))
g.add((Operation6, hctl.hasOperationType, td.readProperty))
g.add((Operation6, hctl.hasTarget, m2target))
g.add((machine6, td.isObservable, falsest))
g.add((machine6, td.name, Literal("Vitesse_Deplacement_X")))


g.add((Workshop, td.hasPropertyAffordance, machine7))
g.add((machine7, rdf.type, td.PropertyAffordance))
g.add((machine7, rdf.type, js.IntegerSchema))
g.add((machine7, rdf.type, onto.XCoordinate))
g.add((machine7, dct.title, Literal("Position Z")))
g.add((machine7, dct.description, Literal("It is used to read the speed of the cartesian motor on Z-Axis", lang=("en"))))
g.add((machine7, js.readOnly, truest))
g.add((machine7, js.writeOnly, falsest))
g.add((machine7, td.hasForm, Operation7))             
g.add((Operation7, rdf.type, hctl.Form))
g.add((Operation7, htv.methodName, Literal("GET")))
g.add((Operation7, hctl.forContentType, Literal("application/json")))
g.add((Operation7, hctl.hasOperationType, td.readProperty))
g.add((Operation7, hctl.hasTarget, m4target))
g.add((machine7, td.isObservable, falsest))
g.add((machine7, td.name, Literal("Vitesse_Deplacement_Z")))

print(g.serialize(r"C:\Users\Siva Ratnam Pachava\OneDrive\Desktop\InternshipM1\VL10\vl10.ttl" , format='ttl'))                                    