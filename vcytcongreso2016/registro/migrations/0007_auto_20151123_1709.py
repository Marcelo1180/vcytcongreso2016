# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_pais_iso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='iso',
            field=models.CharField(max_length=2),
        ),
    ]
