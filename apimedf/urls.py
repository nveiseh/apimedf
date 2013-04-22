from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#REFERENCES URL PATTERNS AT THE SERVER LEVEL
urlpatterns = patterns('',
    url(r'^portal/', include('portal.urls', namespace = "portal")),
    #ADDED for index page to portal, so we INCLUDE the urls.py from the portal app directory
    #so if we go to the main server 0.0.0.0:8000/portal, we are directed to the index view of this app
    # Examples:
    #url(r'^$', 'apimedf.views.home', name='home'),
    # url(r'^apimedf/', include('apimedf.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)