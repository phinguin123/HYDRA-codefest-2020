from django.db import models

# Create your models here.

class Graph(models.Model):
	title 		= models.CharField(max_length=20)

