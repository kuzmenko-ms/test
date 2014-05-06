from django.contrib import admin
import pytz
import datetime
from django.shortcuts import redirect, render
from polls.models import Project
from polls.models import Components


admin.site.register(Project)
admin.site.register(Components)
# Register your models here.
