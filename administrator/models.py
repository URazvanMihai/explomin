from django.db import models

# Create your models here.

class People(models.Model):
   name = models.CharField(max_length=80)
   

  
class Locations(models.Model):
   location = models.CharField(max_length=80)