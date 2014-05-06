from django.db import models
from django.utils import timezone
import datetime
import pytz
from django.shortcuts import redirect, render
#from django_enumfield import enum

class Project(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
    descr = models.CharField(max_length=255)
    content = models.TextField(max_length=10000)
    def _unicode_(self):
        return self.title
    def get_absolute_url(self):
	return "/polls/%i/" % self.id

class Component_type(models.Model):
    type_name = models.IntegerField()
    


class Components(models.Model):	
    #id_c = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    type_c = models.ForeignKey(Component_type) #enum.EnumField(Component_type, default=Component_type.Component_A)
    def _unicode_(self):
        return self.name
    
class Variants(models.Model):
    project = models.ForeignKey(Project)
    type_c = models.ForeignKey(Component_type)#type_c = enum.EnumField(Component_type, default=Component_type.Component_A)
    num = models.CharField(max_length=255)
    def _unicode_(self):
        return self.name


class Pvar1_var2(models.Model):
    pvar = models.ForeignKey(Variants)
    p = models.FloatField()
    u = models.FloatField()
  
class Var_comp(models.Model):
    variants = models.ForeignKey(Variants)
    components = models.ForeignKey(Components)

# Create your models here.
