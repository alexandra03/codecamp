from django.db import models

class Child(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	country = models.CharField(max_length=50)
	interests = models.CharField(max_length=50)
	income = models.IntegerField()
	sponsored = models.BooleanField(default=False)
	vip = models.BooleanField(default=False)