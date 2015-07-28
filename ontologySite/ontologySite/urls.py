from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.mainPage, name='mainPage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^entitis/(?P<entity_id>[0-9]+)/$', views.entity, name='entity'),
    url(r'^entitis/(?P<entity_id>[0-9]+)/update$', views.entityUpdate, name='entityUpdate'),
    url(r'^entitis/add/$', views.entityAdd, name='entityAdd'),
]
