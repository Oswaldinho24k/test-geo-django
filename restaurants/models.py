from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.



class Restaurant (models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	raiting = models.IntegerField(blank=True, null=True,validators=[
            					MaxValueValidator(4),
            					MinValueValidator(1)])
	name    = models.CharField(max_length=200, blank=True, null=True)
	site    = models.CharField(max_length=500, blank=True, null=True)
	email   = models.EmailField(blank=True, null=True)
	phone   = models.CharField(max_length=100, blank=True, null=True)
	street  = models.CharField(max_length=100, blank=True, null=True)
	city    = models.CharField(max_length=100, blank=True, null=True)
	state   = models.CharField(max_length=100, blank=True, null=True)
	lat     = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
	lng     = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)



	def __str__(self):
		return self.name

	def get_point(self):
		return '({}, {})'.format(self.lat, self.lng)

        

