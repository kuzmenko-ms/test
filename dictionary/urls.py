from django.conf.urls import patterns, include, url
from dictionary.views import varvar

 
urlpatterns = patterns('',
 
url(r'^var/$',varvar, name='varvar'),
   
)
