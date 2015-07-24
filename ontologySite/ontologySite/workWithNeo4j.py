# -*- coding: utf-8 -*-
from py2neo import Graph, authenticate

authenticate("localhost:7474", "neo4j", "123")
graph = Graph("http://localhost:7474/db/data/")
        
class Entity:
    def __init__(self,  objectId, objectType, objectName, objectDescription):
        self.id = objectId
        self.type = objectType
        self.name = objectName
        self.description = objectDescription

def entityById(entityId):
    request = graph.cypher.execute("MATCH (entity:Entity) WHERE id(entity) = {} RETURN id(entity), entity.type, entity.name, entity.description".format(entityId))
    entity = request[0]    
    return Entity(entity[0], entity[1], entity[2], entity[3])
    
def allEntities():
    request = graph.cypher.execute("MATCH (nodes:Entity) RETURN id(nodes), nodes.type, nodes.name, nodes.description")
    return [Entity(node[0], node[1], node[2], node[3]) for node in request]

def getParents(objectId):
    request = graph.cypher.execute("MATCH (obj1-[rel:Using_in]->obj2) WHERE id(obj1) = {} RETURN id(obj2), obj2.type, obj2.name, obj2.description".format(objectId))
    return [Entity(entity[0], entity[1], entity[2], entity[3]) for entity in request]
    
def getChildrens(objectId):
    request = graph.cypher.execute("MATCH (obj1-[rel:Using_in]->obj2) WHERE id(obj2) = {} RETURN id(obj1), obj1.type, obj1.name, obj1.description".format(objectId))
    return [Entity(entity[0], entity[1], entity[2], entity[3]) for entity in request]