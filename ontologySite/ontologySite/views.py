# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from . import workWithNeo4j

def mainPage(request):
    entity_list = workWithNeo4j.allEntities()
    context = RequestContext(request, {'entity_list': entity_list})
    return render(request, 'ontologySite/startPage.html', context)
    
def entity(request, entity_id):
    entity = workWithNeo4j.entityById(entity_id)
    childrens = workWithNeo4j.getChildrens(entity_id)
    parents = workWithNeo4j.getParents(entity_id)
    context = RequestContext(request, {'entity': entity, 'childrens': childrens, 'parents': parents})
    return render(request, 'ontologySite/entity.html', context)