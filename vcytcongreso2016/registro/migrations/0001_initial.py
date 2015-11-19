# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields
import registro.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departamento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Frascati_categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frascati_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Frascati_nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frascati_nivel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Investigador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('pasaporte', models.CharField(max_length=50)),
                ('lugar_nacimiento', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=1, choices=[(b'F', b'Femenino'), (b'M', b'Masculino')])),
                ('email', models.EmailField(max_length=254)),
                ('email_institucional', models.EmailField(default=b'', max_length=254)),
                ('foto', models.ImageField(upload_to=b'uploads/foto')),
                ('profesion', models.CharField(max_length=100)),
                ('max_grado', models.CharField(max_length=50)),
                ('max_grado_upload', models.FileField(upload_to=b'uploads/max_grado')),
                ('max_grado_year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014)])),
                ('universidad_profesion', models.CharField(max_length=100)),
                ('universidad_postgrado', models.CharField(max_length=100)),
                ('institucion', models.CharField(max_length=50)),
                ('institucion_ciudad', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=150)),
                ('experiencia_year', models.IntegerField(validators=[registro.models.validate_cant_year])),
                ('curriculum', models.FileField(upload_to=b'uploads/curriculum')),
                ('publicacion', models.CharField(max_length=50)),
                ('ciudad_origen', models.CharField(max_length=100)),
                ('aeropuerto_origen', models.CharField(max_length=100)),
                ('fecha_llegada', models.DateField()),
                ('fecha_retorno', models.DateField()),
                ('comment', models.TextField()),
                ('frascati_categoria', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'frascati_nivel', to='registro.Frascati_categoria', chained_field=b'frascati_nivel')),
                ('frascati_nivel', models.ForeignKey(to='registro.Frascati_nivel')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='investigador',
            name='institucion_pais',
            field=models.ForeignKey(related_name='institucion_pais', to='registro.Pais'),
        ),
        migrations.AddField(
            model_name='investigador',
            name='nacionalidad_actual',
            field=models.ForeignKey(related_name='nacionalidad_actual', to='registro.Pais'),
        ),
        migrations.AddField(
            model_name='investigador',
            name='nacionalidad_origen',
            field=models.ForeignKey(related_name='nacionalidad_origen', to='registro.Pais'),
        ),
        migrations.AddField(
            model_name='investigador',
            name='pais_origen',
            field=models.ForeignKey(related_name='pais_origen', to='registro.Pais'),
        ),
    ]
