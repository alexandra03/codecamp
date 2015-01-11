from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.core import serializers

from app.models import Child

import json

def home(request):
	''' Get list of children, turn it into json, send to and load template '''
	child_list = json.loads(serializers.serialize('json', Child.objects.all(), fields=('name', 'age', 'country', 'income', 'interests', 'photo', 'id')))
	return HttpResponse(loader.get_template('index.html').render(Context({'child_list':child_list})))