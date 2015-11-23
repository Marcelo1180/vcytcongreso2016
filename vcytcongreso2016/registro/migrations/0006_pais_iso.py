# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_auto_20151123_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='iso',
            field=models.CharField(default=b'', max_length=2),
        ),
    ]
