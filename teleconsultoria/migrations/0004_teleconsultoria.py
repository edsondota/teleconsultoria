# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teleconsultoria', '0003_teleconsultor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teleconsultoria',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('agendamento_teleconsultoria', models.DateTimeField()),
                ('status_teleconsultoria', models.CharField(default='AG', choices=[('AT', 'Atendido'), ('CN', 'Cancelado'), ('AG', 'Aguardando')], max_length=2)),
                ('solicitante', models.ForeignKey(to='teleconsultoria.Solicitante')),
                ('teleconsultor', models.ForeignKey(to='teleconsultoria.Teleconsultor')),
            ],
        ),
    ]
