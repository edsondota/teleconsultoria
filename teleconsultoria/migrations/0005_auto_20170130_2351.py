# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teleconsultoria', '0004_teleconsultoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitante',
            name='cpf',
            field=models.CharField(unique=True, max_length=11),
        ),
    ]
