from django.contrib import admin
import pytz
import datetime
from django.shortcuts import redirect, render
from polls.models import Project
from polls.models import Components
from polls.models import Variants,Pvar1_var2,Var_comp,Pvar_var


admin.site.register(Project)
admin.site.register(Components)
admin.site.register(Pvar1_var2)
admin.site.register(Pvar_var)
admin.site.register(Var_comp)
admin.site.register(Variants)
# Register your models here.
