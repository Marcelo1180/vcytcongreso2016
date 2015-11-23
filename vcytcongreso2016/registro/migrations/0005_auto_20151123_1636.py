# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_auto_20151123_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigador',
            name='comment_no',
            field=models.TextField(help_text=b'Comentar por que no puede asistir al evento', verbose_name=b'Comentarios'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='disponibilidad',
            field=models.BooleanField(choices=[(True, b'Si'), (False, b'No')]),
        ),
    ]
