# -*- coding: utf-8 -*-
from py2neo import Graph, authenticate

authenticate("localhost:7474", "neo4j", "123") #авторизация в БД, если вы вводили другой пароль или логин, то нужно заменить "neo4j" и "123" на ваши логин и пароль
graph = Graph("http://localhost:7474/db/data/")

def addEntity(entityType, entityName, entityDescription):
    """ Создает узел. Возвращает его ID. """
    request = graph.cypher.execute("CREATE (node:Entity {type: '" + entityType + "', name: '" + entityName + "', description: '" + entityDescription + "'}) RETURN id(node)")
    return request[0][0]

def updateEntity(entityId, entityType, entityName, entityDescription):
    """ По указанному ID ищет нужный узел, а затем меняет все его поля на указанные. """
    graph.cypher.execute("MATCH (node:Entity) WHERE id(node) = " + str(entityId) + " SET node.type = '" + entityType + "', node.name = '" + entityName + "', node.description = '" + entityDescription + "'")

def removeEntity(entityId):
    """ По указанному ID ищет нужный узел, а затем удаляет его. """
    graph.cypher.execute("MATCH (node:Entity) WHERE id(node) = " + str(entityId) + " DELETE node")

def addRelation(entityOneId, entityTwoId, relationType="Using_in"):
    """ Находит узел №1 с ID == entityOneId, и узел №2 с ID == entityTwoId. Затем создает между ними связь №1-relationType->№2"""
    graph.cypher.execute("MATCH (node1:Entity) WHERE id(node1) = " + str(entityOneId) + " MATCH (node2:Entity) WHERE id(node2) = " + str(entityTwoId) + " CREATE (node1)-[:" + relationType + "]->(node2)")
    
def removeRelation(entityOneId, entityTwoId, relationType="Using_in"):
    """ Находит узел №1 с ID == entityOneId, и узел №2 с ID == entityTwoId. Затем удаляет между ними связь relationType"""
    graph.cypher.execute("MATCH (node1:Entity)-[rel:" + str(relationType) + "]->(node2:Entity) WHERE id(node1) = " + str(entityOneId) + " AND id(node2) = " + str(entityTwoId) + " DELETE rel")
    
def getId(entityName):
    """ По указанному имени ищет нужный node и возвращает его ID. """
    request = graph.cypher.execute("MATCH (node:Entity {name: '" + entityName + "'}) RETURN id(node)")
    return request[0][0]

def getType(entityId):
    """ По указанному ID ищет нужный узел и возвращает его тип(теорема, определение и т.д.). """
    request = graph.cypher.execute("MATCH (node:Entity) WHERE id(node) = " + str(entityId) + " RETURN node.type")
    return request[0][0]
    
def getName(entityId):
    """ По указанному ID ищет нужный узел и возвращает его название. """
    request = graph.cypher.execute("MATCH (node:Entity) WHERE id(node) = " + str(entityId) + " RETURN node.name")
    return request[0][0]
    
def getDescription(entityId):
    """ По указанному ID ищет нужный узел и возвращает его описание. """
    request = graph.cypher.execute("MATCH (node:Entity) WHERE id(node) = " + str(entityId) + " RETURN node.description")
    return request[0][0]
    
def removeAll():
    """ Удаляет все узлы и связи меежду ними. """
    graph.cypher.execute("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")