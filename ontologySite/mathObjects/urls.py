# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^theorems/$', views.theoremList, name='theoremList'),
    url(r'^theorems/(?P<theorem_id>[0-9]+)/$', views.theorem, name='theorem'),
    url(r'^definitions/$', views.definitionList, name='definitionList'),
    url(r'^definitions/(?P<definition_id>[0-9]+)/$', views.definition, name='definition')
]