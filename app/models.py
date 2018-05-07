"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    periodo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=200)

class Vestibular(models.Model):
    nome = models.CharField(max_length=200)

class Candidato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    
class Localprova(models.Model):
    instituicao = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    data = models.CharField(max_length=50)
