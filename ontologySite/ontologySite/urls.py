from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.mainPage, name='mainPage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^entities/(?P<entity_id>[0-9]+)/$', views.entity, name='entity'),
    url(r'^update-entity/(?P<entity_id>[0-9]+)$', views.entityUpdate, name='entityUpdate'),
    url(r'^create-entity/$', views.entityAdd, name='entityAdd'),
    url(r'^entities/[0-9]+/search/$', views.search_titles, name='search_titles'),
    url(r'^search/$', views.search_titles, name='search_titles'),
]
