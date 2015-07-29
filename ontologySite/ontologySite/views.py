# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from . import workWithNeo4j
from .workWithNeo4j import Entity
from django.core.context_processors import csrf

def mainPage(request):
	args = {}
	args.update(csrf(request))
	args['entitis'] = workWithNeo4j.allEntities()
	return render_to_response('ontologySite/startPage.html', args)

    
def entity(request, entity_id):

	args = {}
	args.update(csrf(request))
	args['entity'] = workWithNeo4j.entityById(entity_id)
	args['childrens'] = workWithNeo4j.getChildrens(entity_id)
	args['parents'] = workWithNeo4j.getParents(entity_id)
	return render_to_response('ontologySite/entity.html', args)

def search_titles(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''

	allentitis = workWithNeo4j.allEntities()
	entitis = list()
	for entity in allentitis:
		if search_text in entity.name:
			entitis.append( entity )

	#entitis = workWithNeo4j.objects.filter(name__contains = search_text)

	return render_to_response('ajax_search.html', {'entitis' : entitis, 'length': len(entitis)})