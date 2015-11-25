# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0009_auto_20151125_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigador',
            name='disponibilidad',
            field=models.BooleanField(default=False, choices=[(True, b'Si'), (False, b'No')]),
        ),
    ]
