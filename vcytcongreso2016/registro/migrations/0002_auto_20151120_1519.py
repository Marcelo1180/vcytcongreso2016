# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields
import registro.models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='frascati_categoria',
            name='frascati_nivel',
            field=models.ForeignKey(default=0, to='registro.Frascati_nivel'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='aeropuerto_origen',
            field=models.CharField(max_length=100, verbose_name=b'Aeropuerto de origen'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='ciudad_origen',
            field=models.CharField(max_length=100, verbose_name=b'Ciudad de origen'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='comment',
            field=models.TextField(verbose_name=b'Comentarios'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='curriculum',
            field=models.FileField(upload_to=b'uploads/curriculum', verbose_name=b'Curriculum Vitae'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'Email personal'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='email_institucional',
            field=models.EmailField(default=b'', max_length=254, verbose_name=b'Email institucional'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='experiencia_year',
            field=models.IntegerField(verbose_name=b'A\xc3\xb1os de experiencia', validators=[registro.models.validate_cant_year]),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='fecha_llegada',
            field=models.DateField(verbose_name=b'Fecha de llegada a Bolivia(Cochabamba)'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name=b'Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='fecha_retorno',
            field=models.DateField(verbose_name=b'Fecha de retorno'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='foto',
            field=models.ImageField(upload_to=b'uploads/foto', verbose_name=b'Fotografia 3x3(cm)'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='frascati_categoria',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'frascati_nivel', to='registro.Frascati_categoria', chained_field=b'frascati_nivel', verbose_name=b'Area de investigacion'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='frascati_nivel',
            field=models.ForeignKey(verbose_name=b'Area de investigacion', to='registro.Frascati_nivel'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='institucion',
            field=models.CharField(max_length=50, verbose_name=b'Institucion'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='institucion_ciudad',
            field=models.CharField(max_length=50, verbose_name=b'Ciudad'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='institucion_pais',
            field=models.ForeignKey(related_name='Pais', to='registro.Pais'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='lugar_nacimiento',
            field=models.CharField(max_length=100, verbose_name=b'Lugar de nacimiento'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='max_grado',
            field=models.CharField(max_length=50, verbose_name=b'Maximo grado academico'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='max_grado_upload',
            field=models.FileField(upload_to=b'uploads/max_grado', verbose_name=b'Adjuntar copia digital del titulo'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='max_grado_year',
            field=models.IntegerField(verbose_name=b'A\xc3\xb1o de obtencion', choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014)]),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='nacionalidad_actual',
            field=models.ForeignKey(related_name='nacionalidad_actual', verbose_name=b'Nacionalidad actual', to='registro.Pais', help_text=b'Especifique la nacionalidad que utiliza actualmente de manera legal'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='nacionalidad_origen',
            field=models.ForeignKey(related_name='nacionalidad_origen', verbose_name=b'Nacionalidad de origen', to='registro.Pais', help_text=b'Ingrese la nacionalidad que recibio al momento de nacer aunque esta haya cambiado luego de ese momento'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='nombre_completo',
            field=models.CharField(max_length=100, verbose_name=b'Nombre y Apellidos'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='pais_origen',
            field=models.ForeignKey(related_name='pais_origen', verbose_name=b'Pa\xc3\xads de origen', to='registro.Pais'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='publicacion',
            field=models.CharField(max_length=50, verbose_name=b'Colocar el enlace'),
        ),
    ]
