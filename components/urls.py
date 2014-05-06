from django.conf.urls import patterns, url
from polls.views import ProjectsListView, ProjectsDetailView,ComponentsListView
from components.views import dictionary,delete_comp

urlpatterns = patterns('',
url(r'^$',dictionary, name='dictionary'),
url(r'^del/(?P<id_c>\d+)/$',delete_comp, name='delete_comp'),
)
