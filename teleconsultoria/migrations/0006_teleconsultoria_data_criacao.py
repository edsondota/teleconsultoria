# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teleconsultoria', '0005_auto_20170130_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='teleconsultoria',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 1, 31, 0, 30, 6, 744433, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
