from django.test import TestCase
from django.contrib.auth.models import User
from teleconsultoria.models import Administrador, Solicitante


class AdministradorTest(TestCase):
    def test_cria_administrador(self):
        """ Testando se é possível criar um objeto Administrador """
        user_administrador = User.objects.create(username="administrador", password="123", email="admin@email.com", is_superuser=True)
        administrador = Administrador.objects.create(user=user_administrador)
        self.assertTrue(administrador)


class SolicitanteTest(TestCase):
    def test_cria_solicitante(self):
        """ Testando se é possível criar um objeto Solicitante """
        user_solicitante = User.objects.create(username="solicitante", password="123", email="solicitante@email.com")
        solicitante = Solicitante.objects.create(user=user_solicitante, nome=u"João Silva", telefone="551122336655", cpf="11122233344")
        self.assertTrue(solicitante)
