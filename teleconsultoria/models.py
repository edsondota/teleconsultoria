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


class Teleconsultoria(models.Model):
    ATENDIDO = 'AT'
    CANCELADO = 'CN'
    AGUARDANDO = 'AG'
    STATUS_CHOICES = (
        (ATENDIDO, 'Atendido'),
        (CANCELADO, 'Cancelado'),
        (AGUARDANDO, 'Aguardando'),
    )
    teleconsultor = models.ForeignKey('Teleconsultor')
    solicitante = models.ForeignKey('Solicitante')
    agendamento_teleconsultoria = models.DateTimeField()
    status_teleconsultoria = models.CharField(max_length=2,
            choices=STATUS_CHOICES, default=AGUARDANDO)
