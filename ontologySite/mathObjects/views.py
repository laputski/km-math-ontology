from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from . import workWithNeo4j
    
def index(request):
    template = loader.get_template('mathObjects/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def entity(request, entity_id):
    entity = workWithNeo4j.entityById(entity_id)
    childrens = workWithNeo4j.getChildrens(entity_id)
    parents = workWithNeo4j.getParents(entity_id)
    context = RequestContext(request, {'entity': entity, 'childrens': childrens, 'parents': parents})
    return render(request, 'mathObjects/entity.html', context)
    
def entityList(request):
    entity_list = workWithNeo4j.allEntities()
    template = loader.get_template('mathObjects/entityList.html')
    context = RequestContext(request, {'entity_list': entity_list,})
    return HttpResponse(template.render(context))

def graph(request):
    template = loader.get_template('mathObjects/graph.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))