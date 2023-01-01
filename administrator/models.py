from django.db import models

# Create your models here.

class People(models.Model):
   name = models.CharField(max_length=80)
   

  
class Locations(models.Model):
   location = models.CharField(max_length=80)



class Pontaj(models.Model):
   id = models.AutoField(primary_key=True)
   ruta = models.CharField(max_length = 100)
   km = models.DecimalField( max_digits=5, decimal_places=2)
   ore =  models.DecimalField( max_digits=5, decimal_places=2)
   observatii = models.CharField(max_length = 100)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


   def __str__ (self):
    template = '{0.ruta} {0.km} {0.ore} {0.observatii}'
    return template.format(self)

class PontajToggleEdit(models.Model):
    id = models.AutoField(primary_key=True)
    pontaj_id = models.IntegerField(null=True)
    is_edit_mode = models.BooleanField(default=False)

class Masini(models.Model):
    id = models.AutoField(primary_key=True)
    numar = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)

class Puscari(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.CharField(max_length=5, null=True)
    cariera = models.CharField(max_length=150)
    ziua = models.DateField(auto_now_add=False, auto_now=False, null=True)
    ora = models.TimeField(auto_now=False, auto_now_add=False)
    nume_coordonator = models.CharField(max_length=150)
    masina_coordonator = models.CharField(max_length=150)
    nume_artificier = models.CharField(max_length=150)
    masina_artificier = models.CharField(max_length=150)
    nume_azot = models.CharField(max_length=150)
    masina_azot = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PuscareMembriiEchipei(models.Model):
    id = models.AutoField(primary_key=True)
    puscare_id = models.IntegerField(null=False)
    nume_membru = models.CharField(max_length=150)
    masina_membru = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)