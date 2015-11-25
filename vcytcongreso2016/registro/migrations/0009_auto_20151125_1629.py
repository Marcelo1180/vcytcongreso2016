# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0008_auto_20151124_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigador',
            name='disponibilidad',
            field=models.BooleanField(help_text=b'Marque aqui si dispone de tiempo para asistir al evento', choices=[(True, b'Si'), (False, b'No')]),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='email_institucional',
            field=models.EmailField(default=b'', max_length=254, verbose_name=b'Email institucional', blank=True),
        ),
    ]
