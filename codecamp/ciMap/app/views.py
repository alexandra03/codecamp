from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.core import serializers

from app.models import Child

import json

def home(request):
	child_list = json.loads(serializers.serialize('json', Child.objects.all(), fields=('name', 'age', 'country', 'income', 'interests', 'photo', 'id')))
	template = loader.get_template('index.html')
	context = Context({'child_list':child_list})
	return HttpResponse(template.render(context))
