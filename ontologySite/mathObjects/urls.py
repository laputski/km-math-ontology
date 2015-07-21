# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^entities/$', views.entityList, name='entityList'),
    url(r'^entities/(?P<entity_id>[0-9]+)/$', views.entity, name='entity'),
    url(r'^graph/$', views.graph, name='graph')
]