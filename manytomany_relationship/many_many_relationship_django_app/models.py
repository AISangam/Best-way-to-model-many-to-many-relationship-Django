from django.db import models

# Create your models here.
class bags(models.Model):
	brand = models.CharField(max_length=50)
	capacity=models.CharField(max_length=10)

	def __str__(self):
		return "%s" % (self.brand)

class buyers(models.Model):
	name = models.CharField(max_length=70)
	age = models.IntegerField(max_length=10)
	bags_purchased = models.ManyToManyField(bags)		

	def __str__(self):
		return "%s" % (self.name)
		