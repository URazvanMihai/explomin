from django.db import models

# Create your models here.

class People(models.Model):
   name = models.CharField(max_length=80)
   

  
class Locations(models.Model):
   location = models.CharField(max_length=80)



class Postform(models.Model):
   id = models.AutoField(primary_key=True)
   ruta = models.CharField(max_length = 100)
   km = models.DecimalField( max_digits=5, decimal_places=2)
   ore =  models.DecimalField( max_digits=5, decimal_places=2)
   observatii = models.CharField(max_length = 100)


   def __str__ (self):

      return(self.ruta,
            self.km,
            self.ore,
            self.observatii)