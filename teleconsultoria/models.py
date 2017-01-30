from django.db import models
from django.contrib.auth.models import User

class Administrador(models.Model):
    user = models.ForeignKey(User)
