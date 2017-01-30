from django.db import models
from django.contrib.auth.models import User

class Administrador(models.Model):
    user = models.ForeignKey(User)


class Solicitante(models.Model):
    user = models.ForeignKey(User)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=25)
    cpf = models.CharField(max_length=11)
    

class Teleconsultor(models.Model):
    user = models.ForeignKey(User)
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=10)
    data_formatura = models.DateField()
