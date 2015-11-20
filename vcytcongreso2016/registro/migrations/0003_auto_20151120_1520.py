# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20151120_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frascati_categoria',
            name='frascati_nivel',
            field=models.ForeignKey(to='registro.Frascati_nivel'),
        ),
    ]
