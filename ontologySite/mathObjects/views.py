from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Theorem

def index(request):
    theorem_list = Theorem.objects.all()
    template = loader.get_template('mathObjects/index.html')
    context = RequestContext(request, {'theorem_list': theorem_list,})
    return HttpResponse(template.render(context))

def theorem(request, theorem_id):
    theorem = get_object_or_404(Theorem, pk=theorem_id)
    context = RequestContext(request, {'theorem': theorem,})
    return render(request, 'mathObjects/theorem.html', context)