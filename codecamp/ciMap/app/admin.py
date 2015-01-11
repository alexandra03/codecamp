from django.contrib import admin
from app.models import *

class childInfo(admin.ModelAdmin):
	def show_url(obj):
		return u"<a href='%s' target='_blank'>Picture</a>" % (obj.photo)
	show_url.allow_tags = True
	list_display = ('name', 'age', 'country', 'income', 'interests', show_url)
	list_filter = ['age', 'country']

admin.site.register(Child, childInfo)