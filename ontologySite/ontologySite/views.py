# -*- coding: utf-8 -*-        
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from . import workWithNeo4j
from django.core.context_processors import csrf

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
        
    args = {}
    args.update(csrf(request))
    args['entitiesList'] = entity_list
    return render_to_response('ontologySite/startPage.html', args)
    
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
    
    args = {}
    args.update(csrf(request))
    args['entity'] = workWithNeo4j.entityById(entity_id)
    args['childrens'] = workWithNeo4j.getChildrens(entity_id)
    args['parents'] = workWithNeo4j.getParents(entity_id)
    args['entitiesList'] = entity_list
    
    return render_to_response('ontologySite/entity.html', args)
    
def entityUpdate(request, entity_id):
    entity = workWithNeo4j.entityById(entity_id)
    childrens = workWithNeo4j.getChildrens(entity_id)
    parents = workWithNeo4j.getParents(entity_id)
    context = RequestContext(request, {'entity': entity, 'childrens': childrens, 'parents': parents})
    return render(request, 'ontologySite/entityUpdate.html', context)
    
def entityAdd(request):
    context = RequestContext(request, {})
    return render(request, 'ontologySite/entityAdd.html', context)

def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    allentitis = workWithNeo4j.allEntities()
    entitiesList = list()
    for entity in allentitis:
            if search_text in entity.name:
                entitiesList.append( entity )

    #entitis = workWithNeo4j.objects.filter(name__contains = search_text)

    return render_to_response('ajax_search.html', {'entitiesList' : entitiesList, 'length': len(entitiesList)})