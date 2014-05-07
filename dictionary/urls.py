from django.conf.urls import patterns, include, url
from dictionary.views import varvar,add_var

 
urlpatterns = patterns('',
 
url(r'^var/$',varvar, name='varvar'),
url(r'^addvar/$',add_var, name='add_var'),
   
)
