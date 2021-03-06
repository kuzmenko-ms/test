from django.template import RequestContext
from polls.models import Project,Pvar1_var2,Variants
from polls.models import Components
from polls.models import Component_type
from django.views.generic import ListView, DetailView
from django.forms import ModelForm
from django.shortcuts import render
import random
import json
from django.utils import simplejson
from django.shortcuts import HttpResponse

# Create your views here.
class ProjectsListView(ListView):
	model = Project

class ProjectsDetailView(DetailView):
	model = Project

class ComponentsListView(ListView):
	model = Components

def project_view(request, pk):
    model_variants = Variants.objects.all()
    model_p_u = Pvar1_var2.objects.all()
    data = [{"u":str(x.u*10), "sorned" : x.p} for  x in model_p_u]
    '''data = [     
            {"u": "23.34",  "sorned": 467},
            {"u": "24.37 ", "sorned": 646},
            {"u": "25.39",  "sorned":323},
            {"u": "26.56",  "sorned": 245},
            {"u": "27.89",  "sorned": 654}
           ]'''
    data.sort()
    project = Project.objects.filter(id=pk)[0]
    return render(request, 'polls/project_detail.html', {'plot_data' : simplejson.dumps(data), 'project' : project, 'model_variants' : model_variants })




  
