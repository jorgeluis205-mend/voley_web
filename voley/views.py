from django.http import HttpResponse
from django.template import loader
from .models import Persona
from django.shortcuts import render

def personas(request):
  mispersonas = Persona.objects.all().values()
  template = loader.get_template('todos_personas.html')
  context = {
    'mispersonas': mispersonas,
  }
  return HttpResponse(template.render(context, request))

def tables(request):
 return render(request, 'voley/index.html')
 #return render(request, 'datatables.html')