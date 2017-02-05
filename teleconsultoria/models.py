import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Administrador(models.Model):
    user = models.ForeignKey(User)


class Solicitante(models.Model):
    user = models.OneToOneField(User)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=25)
    cpf = models.CharField(max_length=11, unique=True)

    @property
    def pode_criar_teleconsultoria(self):
        dia_atual = datetime.datetime.now()
        teleconsultoria = self.teleconsultoria_set.filter(solicitante=self,
                data_criacao__year=dia_atual.year,
                data_criacao__month=dia_atual.month,
                data_criacao__day=dia_atual.day)
        if teleconsultoria:
            return False
        return True
    

class Teleconsultor(models.Model):
    user = models.OneToOneField(User)
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=10)
    data_formatura = models.DateField()


class Teleconsultoria(models.Model):
    ACEITA = 'AC'
    CANCELADO = 'CN'
    AGUARDANDO = 'AG'
    STATUS_CHOICES = (
        (ACEITA, 'Aceita'),
        (CANCELADO, 'Cancelado'),
        (AGUARDANDO, 'Aguardando'),
    )
    teleconsultor = models.ForeignKey('Teleconsultor')
    solicitante = models.ForeignKey('Solicitante')
    agendamento_teleconsultoria = models.DateTimeField()
    status_teleconsultoria = models.CharField(max_length=2,
            choices=STATUS_CHOICES, default=AGUARDANDO)
    data_criacao = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            dia_atual = datetime.datetime.now()
            teleconsultoria = Teleconsultoria.objects.filter(solicitante=self.solicitante,
                    data_criacao__year=dia_atual.year,
                    data_criacao__month=dia_atual.month,
                    data_criacao__day=dia_atual.day)
            if teleconsultoria:
                raise ValidationError(u'Já existe uma teleconsultoria para este solicitante no dia')
        super(Teleconsultoria, self).save(*args, **kwargs)
