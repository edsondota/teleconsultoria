import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
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
    def setUp(self):
        user_solicitante = User.objects.create(username="solicitante",
                password="123", email="solicitante@email.com")
        solicitante = Solicitante.objects.create(user=user_solicitante,
                nome=u"João Silva", telefone="551122336655", cpf="11122233344")

    def test_cria_solicitante(self):
        """ Testando se é possível criar um objeto Solicitante """
        solicitante = Solicitante.objects.get(cpf="11122233344")
        self.assertTrue(solicitante)

    def test_solicitante_unico(self):
        user_solicitante = User.objects.create(username="solicitante_2",
                password="123", email="solicitante_2@email.com")
        with self.assertRaises(IntegrityError):
            solicitante = Solicitante.objects.create(user=user_solicitante,
                    nome=u"João Silva", telefone="551122336655", cpf="11122233344")


class TeleconsultorTest(TestCase):
    def setUp(self):
        user_teleconsultor = User.objects.create(username="teleconsultor",
                password="123", email="teleconsultor@email.com")
        teleconsultor = Teleconsultor.objects.create(user=user_teleconsultor,
                nome="José Santos", crm="BA-1234", data_formatura=datetime.date(2017, 1, 30))

    def test_cria_teleconsultor(self):
        """ Testando se é possível criar um objeto Teleconsultor """
        teleconsultor = Teleconsultor.objects.get(crm='BA-1234')
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

    def test_cria_teleconsultoria_mesmo_dia(self):
        teleconsultor = Teleconsultor.objects.get(crm='BA-1234')
        solicitante = Solicitante.objects.get(cpf="11122233344")
        teleconsultoria = Teleconsultoria.objects.create(teleconsultor=teleconsultor,
                solicitante=solicitante, agendamento_teleconsultoria=datetime.datetime(2017, 1, 30, 20, 52))
        with self.assertRaises(ValidationError):
            teleconsultoria_2 = Teleconsultoria.objects.create(teleconsultor=teleconsultor,
                    solicitante=solicitante, agendamento_teleconsultoria=datetime.datetime(2017, 1, 30, 20, 52))
