from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from . import workWithNeo4j
    
def index(request):
    template = loader.get_template('mathObjects/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def theorem(request, theorem_id):
    theorem = workWithNeo4j.theoremById(theorem_id)
    useWhat = workWithNeo4j.useWhat(theorem_id)
    usedIn = workWithNeo4j.usedIn(theorem_id)
    context = RequestContext(request, {'theorem': theorem, 'useWhat': useWhat, 'usedIn': usedIn})
    return render(request, 'mathObjects/theorem.html', context)
    
def definition(request, definition_id):
    definition = workWithNeo4j.definitionById(definition_id)
    useWhat = workWithNeo4j.useWhat(definition_id)
    usedIn = workWithNeo4j.usedIn(definition_id)
    context = RequestContext(request, {'definition': definition, 'useWhat': useWhat, 'usedIn': usedIn})
    return render(request, 'mathObjects/definition.html', context)
    
def theoremList(request):
    theorem_list = workWithNeo4j.allTheorems()
    template = loader.get_template('mathObjects/theoremList.html')
    context = RequestContext(request, {'theorem_list': theorem_list,})
    return HttpResponse(template.render(context))
    
def definitionList(request):
    definition_list = workWithNeo4j.allDefinitions()
    template = loader.get_template('mathObjects/definitionList.html')
    context = RequestContext(request, {'definition_list': definition_list})
    return HttpResponse(template.render(context)) 