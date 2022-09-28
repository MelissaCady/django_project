from datetime import date
from email.policy import default
from django.db import models

# Create your models here.
class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  
class Projects(models.Model):
  name_project = models.CharField(max_length=255)
  date_project = models.DateField(default=date.today)
  nb_releve = models.IntegerField( null=True)
  url_site = models.TextField(blank=True)
  
class Releve(models.Model):
  id_releve = models.BigAutoField(primary_key=True)
  name_releve = models.CharField(max_length=255)
  date_releve = models.DateField(default=date.today)
  etat_releve = models.BooleanField(null=True)
  nb_tread_releve = models.IntegerField(blank=True)
  nb_comment_releve = models.IntegerField(blank=True)
  id_members = models.ForeignKey(Members, on_delete=models.CASCADE, default=None)
  id_project = models.ForeignKey(Projects, on_delete=models.CASCADE, default=None)