from django.template import RequestContext
from polls.models import Project,Variants
from polls.models import Pvar_var,Pvar1_var2
from polls.models import Component_type,Components
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

def add_var(request):
    errors = []
    form = {}
    model_vr = Component_type.objects.all()
    model_p = Pvar1_var2.objects.all()
    if request.POST:
        form['project_var'] = request.POST.get('project_var')
        form['name_var'] = request.POST.get('name_var')
        form['type_comp'] = request.POST.get('type_comp')
        form['p'] = request.POST.get('p')
        if not form['name_var']:
            errors.append('error name')
        if not form['type_comp']:
            errors.append('error name')
        if not form['p']:
            errors.append('error name')        
        if not errors:
           
            model1 = Variants(project_id = '53',type_c_id=form['type_comp'],num=form['name_var'],pvar_id=form['p'])
            model1.save()
       
        return render(request, 'polls/var_add.html', {'errors': errors, 'form':form,'model_vr' : model_vr,'model_p' : model_p })
    return render(request, 'polls/var_add.html', {'errors': errors,'model_vr' : model_vr,'model_p' : model_p })

    
