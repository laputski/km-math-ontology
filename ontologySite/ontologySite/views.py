# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from . import workWithNeo4j

def mainPage(request):
    entity_list = workWithNeo4j.allEntities()
    
    for entity in entity_list:
        entity.childrens =  workWithNeo4j.getChildrens(entity.id)
        entity.parents =  workWithNeo4j.getParents(entity.id)
        if entity.type == 'Theorem':
            entity.score = 1
        elif entity.type == 'Definition':
            entity.score = 5
        else: entity.score = 0

    context = RequestContext(request, {'entityList': entity_list})
    return render(request, 'ontologySite/startPage.html', context)
    
def entity(request, entity_id):
    entity_list = workWithNeo4j.allEntities()
    
    for entity in entity_list:
        entity.childrens =  workWithNeo4j.getChildrens(entity.id)
        entity.parents =  workWithNeo4j.getParents(entity.id)
        if str(entity.id) == entity_id:
            entity.score = 10
        elif entity.type == 'Theorem':
            entity.score = 1
        elif entity.type == 'Definition':
            entity.score = 5
        else: entity.score = 0
        
    entity = workWithNeo4j.entityById(entity_id)
    childrens = workWithNeo4j.getChildrens(entity_id)
    parents = workWithNeo4j.getParents(entity_id)
    context = RequestContext(request, {'entity': entity, 'childrens': childrens, 'parents': parents, 'entityList': entity_list})
    return render(request, 'ontologySite/entity.html', context)
    
def entityUpdate(request, entity_id):
    entity = workWithNeo4j.entityById(entity_id)
    childrens = workWithNeo4j.getChildrens(entity_id)
    parents = workWithNeo4j.getParents(entity_id)
    context = RequestContext(request, {'entity': entity, 'childrens': childrens, 'parents': parents})
    return render(request, 'ontologySite/entityUpdate.html', context)
    
def entityAdd(request):
    context = RequestContext(request, {})
    return render(request, 'ontologySite/entityAdd.html', context)