from django.core.urlresolvers import reverse  
from djangorestframework.resources import ModelResource  
from polls.models import Project 
  
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "name","descr","content"]
 
 
 
