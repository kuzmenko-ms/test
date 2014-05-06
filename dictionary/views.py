from django.template import RequestContext
from polls.models import Project,Variants
from polls.models import Pvar_var
from polls.models import Component_type
from django.views.generic import ListView, DetailView
from django.forms import ModelForm
from django.shortcuts import redirect
import random
import json
from django.shortcuts import HttpResponse
from django.shortcuts import render

def varvar(request):
    model_p_vv = Pvar_var.objects.all()
    model_var = Variants.objects.all()
    errors = []
    form = {}
    if request.POST:
        form['type_var1'] = request.POST.get('type_var1')
        form['type_var2'] = request.POST.get('type_var2')
        form['p'] = request.POST.get('p')
        if not form['type_var1']:
            errors.append('error name')
        if not form['type_var2']:
            errors.append('error name')
        if not form['p']:
            errors.append('error name')        
        if not errors:
           
            model1 = Pvar_var(var1_id=form['type_var1'],var2_id=form['type_var2'],p=form['p'])
            model1.save()
       
        return render(request, 'polls/var.html', {'errors': errors, 'form':form, 'model_p_vv' : model_p_vv,'model_var' : model_var })
    return render(request, 'polls/var.html', {'errors': errors, 'model_p_vv' : model_p_vv,'model_var' : model_var })

