# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_auto_20151120_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigador',
            name='comment_no',
            field=models.TextField(default=b'', help_text=b'Comentar por que no puede asistir al evento', verbose_name=b'Comentarios'),
        ),
        migrations.AddField(
            model_name='investigador',
            name='disponibilidad',
            field=models.BooleanField(default=False, choices=[(True, b'Si'), (False, b'No')]),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='frascati_categoria',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'frascati_nivel', to='registro.Frascati_categoria', chained_field=b'frascati_nivel', verbose_name=b'Area de investigacion (Categoria)'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='frascati_nivel',
            field=models.ForeignKey(verbose_name=b'Area de investigacion (Nivel)', to='registro.Frascati_nivel'),
        ),
    ]
