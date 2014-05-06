from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Project
import datetime

 
def project(request):
    errors = []
    form = {}
    model = Project.objects.all()
    if request.POST:
        form['title'] = request.POST.get('title')
        form['name'] = request.POST.get('name')
        form['descr'] = request.POST.get('descr')
        form['content'] = request.POST.get('content')
        if not form['title']:
            errors.append('error title')
        if  not form['name']:
            errors.append('error name')
        if not form['descr']:
            errors.append('error description')
           
        if not form['content']:
            errors.append('error content')
        if not errors:
            model = Project(title=form['title'],name=form['name'],descr=     form['descr'],content=form['content'],datetime=datetime.datetime.now())
            model.save()
       
        return render(request, 'good.html', {'errors': errors, 'form':form, 'model': model})
    return render(request, 'project.html', {'errors': errors, 'form':form, 'model': model})
    
