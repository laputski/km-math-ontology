# -*- coding: utf-8 -*-
from django import forms

class EntityForm(forms.Form):
    entityType = forms.CharField(label='aga1', max_length=20)
    entityName = forms.CharField(label='aga2', max_length=50)
    entityDescription = forms.CharField(label='aga3', max_length=200)