from django.test import TestCase
from teleconsultoria.models import Administrador
from django.contrib.auth.models import User


class AdministradorTest(TestCase):
    def test_cria_administrador(self):
        """ Testando se é possível criar um objeto Administrador """
        user_administrador = User.objects.create(username="administrador", password="123", email="admin@email.com", is_superuser=True)
        administrador = Administrador.objects.create(user=user_administrador)
        self.assertTrue(administrador)
