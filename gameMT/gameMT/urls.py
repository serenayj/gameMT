from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from gameMT.views import * 
from views import * 

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'gameMT.views.home', name='home'),
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'login/$', login_view),
    url(r'register/$', register),
    url(r'logout/$', logout_view),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
