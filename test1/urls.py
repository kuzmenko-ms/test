from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from polls import views
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
admin.autodiscover()

urlpatterns = patterns('',
  
    url(r'^$', 'test1.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('registration.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^components/', include('components.urls')),
    #url(r'^components/','components.views.dictionary', name='dictionary'),
    url(r'^project/', include('project.urls')),
    url(r'^dictionary/', include('dictionary.urls')),
)




    
