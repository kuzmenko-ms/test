from django.conf.urls import patterns, url
from polls.views import ProjectsListView, ProjectsDetailView,ComponentsListView
from components.views import dictionary,delete_comp,delete_proj,delete_var

urlpatterns = patterns('',
url(r'^$',dictionary, name='dictionary'),
url(r'^del/(?P<id_c>\d+)/$',delete_comp, name='delete_comp'),
url(r'^delp/(?P<id_p>\d+)/$',delete_proj, name='delete_proj'),
url(r'^delver/(?P<id_v>\d+)/$',delete_var, name='delete_var'),
)
