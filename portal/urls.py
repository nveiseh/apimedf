from django.conf.urls import patterns, url

from portal import views

#URLS PATTERS AT THE APP LEVEL: 0.0.0.0:8000/portal/...
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    # ex: /portal/csv view
    url(r'^(?P<poll_id>\d+)/csv_view/$', views.csv_view, name='csv_view'),
)