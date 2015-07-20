# -*- coding: utf-8 -*-
from py2neo import Graph, authenticate

authenticate("localhost:7474", "neo4j", "123")
graph = Graph("http://localhost:7474/db/data/")
        
class MathObject:
    def __init__(self, objectType, objectId, objectTitle, objectDescription):
        self.type = objectType
        self.id = objectId
        self.title = objectTitle
        self.description = objectDescription

def theoremById(theoremId):
    request = graph.cypher.execute("MATCH (theorem:Theorem) WHERE id(theorem) = " + str(theoremId) + " RETURN id(theorem), theorem.title, theorem.description")
    theorem = request[0]    
    return MathObject('Theorem', theorem[0], theorem[1], theorem[2])

def definitionById(definitionId):
    request = graph.cypher.execute("MATCH (definition:Definition) WHERE id(definition) = " + str(definitionId) + " RETURN id(definition), definition.title, definition.description")
    definition = request[0]    
    return MathObject('Definition', definition[0], definition[1], definition[2])
    
def allTheorems():
    request = graph.cypher.execute("MATCH (theorems:Theorem) RETURN id(theorems), theorems.title, theorems.description")
    return [MathObject('Theorem', theorem[0], theorem[1], theorem[2]) for theorem in request]
    
def allDefinitions():
    request = graph.cypher.execute("MATCH (definitions:Definition) RETURN id(definitions), definitions.title, definitions.description")
    return [MathObject('Definition', definition[0], definition[1], definition[2]) for definition in request]

def usedIn(objectId):
    request = graph.cypher.execute("MATCH (obj1-[rel:Using_in]->obj2) WHERE id(obj1) = " + str(objectId) + " RETURN id(obj2), obj2.title, obj2.description, labels(obj2)")
    return [MathObject(mathObject[3][0], mathObject[0], mathObject[1], mathObject[2]) for mathObject in request]
    
def useWhat(objectId):
    request = graph.cypher.execute("MATCH (obj1-[rel:Using_in]->obj2) WHERE id(obj2) = " + str(objectId) + " RETURN id(obj1), obj1.title, obj1.description, labels(obj1)")
    return [MathObject(mathObject[3][0], mathObject[0], mathObject[1], mathObject[2]) for mathObject in request]