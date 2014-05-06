from django.template import RequestContext
from polls.models import Project
from polls.models import Components
from polls.models import Component_type
from django.views.generic import ListView, DetailView
from django.forms import ModelForm
from django.shortcuts import redirect
import random
import json
from django.shortcuts import HttpResponse
from django.shortcuts import render


def home(request):
    context = {}
    return render_to_response('login.html', context, RequestContext(request))

#class ComponentsListView(ListView):
	#model = Components
	#model2 = Component_type
def delete_comp(request, id_c):
    model11 = Components.objects.all()
    model = Component_type.objects.all()
    errors = []
    form = {}
    model_d_com = Components.objects.filter(id=id_c)
    if len(model_d_com) > 0:
        model_d_com[0].delete()
    else:
        errors.append('Bad index3')  
    return redirect('/components/')
    
def dictionary(request):
    model11 = Components.objects.all()
    model = Component_type.objects.all()
    errors = []
    form = {}
    if request.POST:
        form['name'] = request.POST.get('name')
        form['type_components'] = request.POST.get('type_components')
        if not form['name']:
            errors.append('error name')
        if not errors:
           
            model1 = Components(name=form['name'],type_c_id=form['type_components'])
            model1.save()
       
        return render(request, 'polls/components_list.html', {'errors': errors, 'form':form, 'model' : model, 'model11' : model11})
    return render(request, 'polls/components_list.html', {'errors': errors, 'form':form, 'model' : model, 'model11' : model11})


