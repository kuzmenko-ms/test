from django.conf.urls import patterns, url
from polls.views import ProjectsListView, ProjectsDetailView,ComponentsListView, project_view

urlpatterns = patterns('',
url(r'^$',ProjectsListView.as_view(), name='list1'),
url(r'^(?P<pk>\d+)/$', project_view),


)
