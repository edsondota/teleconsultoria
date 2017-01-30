import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from teleconsultoria.models import Administrador, Solicitante, Teleconsultor
from teleconsultoria.models import Teleconsultoria


class AdministradorTest(TestCase):
    def test_cria_administrador(self):
        """ Testando se é possível criar um objeto Administrador """
        user_administrador = User.objects.create(username="administrador",
                password="123", email="admin@email.com", is_superuser=True)
        administrador = Administrador.objects.create(user=user_administrador)
        self.assertTrue(administrador)


class SolicitanteTest(TestCase):
    def test_cria_solicitante(self):
        """ Testando se é possível criar um objeto Solicitante """
        user_solicitante = User.objects.create(username="solicitante",
                password="123", email="solicitante@email.com")
        solicitante = Solicitante.objects.create(user=user_solicitante,
                nome=u"João Silva", telefone="551122336655", cpf="11122233344")
        self.assertTrue(solicitante)


class TeleconsultorTest(TestCase):
    def test_cria_teleconsultor(self):
        """ Testando se é possível criar um objeto Teleconsultor """
        user_teleconsultor = User.objects.create(username="teleconsultor",
                password="123", email="teleconsultor@email.com")
        teleconsultor = Teleconsultor.objects.create(user=user_teleconsultor,
                nome="José Santos", crm="BA-1234", data_formatura=datetime.date(2017, 1, 30))
        self.assertTrue(teleconsultor)


class TeleconsultoriaTest(TestCase):
    def setUp(self):
        user_teleconsultor = User.objects.create(username="teleconsultor",
                password="123", email="teleconsultor@email.com")
        Teleconsultor.objects.create(user=user_teleconsultor,
                nome="José Santos", crm="BA-1234", data_formatura=datetime.date(2017, 1, 30))
        user_solicitante = User.objects.create(username="solicitante",
                password="123", email="solicitante@email.com")
        Solicitante.objects.create(user=user_solicitante,
                nome=u"João Silva", telefone="551122336655", cpf="11122233344")
    def test_cria_teleconsultoria(self):
        """ Testando se é possível criar um objeto Teleconsultoria """
        teleconsultor = Teleconsultor.objects.get(crm='BA-1234')
        solicitante = Solicitante.objects.get(cpf="11122233344")
        teleconsultoria = Teleconsultoria.objects.create(teleconsultor=teleconsultor,
                solicitante=solicitante, agendamento_teleconsultoria=datetime.datetime(2017, 1, 30, 20, 52))
        self.assertTrue(teleconsultoria)
