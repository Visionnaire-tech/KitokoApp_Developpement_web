from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Classe(models.Model):
    Nom = models.CharField(max_length=50)
    Post_Nom = models.CharField(max_length=50)
    Prénom = models.CharField(max_length=50)
    faculty = models.ForeignKey('Faculty',on_delete=models.CASCADE)
    cursus = models.ForeignKey('Cursus', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.Nom + " " + self.Post_Nom + " " + self.Prénom

class Faculty(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Cursus(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
class Promotion(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
class Vacation(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class EnvoisTp(Classe):
    
    promotion =models.ForeignKey('Promotion', on_delete=models.CASCADE)
    vacation = models.ForeignKey('Vacation',on_delete=models.CASCADE)
    Séléctionner_Votre_travail = models.FileField(upload_to="PDF")
    
    
