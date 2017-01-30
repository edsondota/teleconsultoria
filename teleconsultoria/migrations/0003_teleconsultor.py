# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teleconsultoria', '0002_solicitante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teleconsultor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('crm', models.CharField(max_length=10)),
                ('data_formatura', models.DateField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
