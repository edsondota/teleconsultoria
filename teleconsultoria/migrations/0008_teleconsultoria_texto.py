# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teleconsultoria', '0007_auto_20170205_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='teleconsultoria',
            name='texto',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
