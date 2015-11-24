# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0007_auto_20151123_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investigador',
            name='frascati_nivel',
        ),
        migrations.AlterField(
            model_name='investigador',
            name='frascati_categoria',
            field=smart_selects.db_fields.GroupedForeignKey(to='registro.Frascati_categoria', group_field=b'frascati_nivel', verbose_name=b'Area de investigaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='max_grado',
            field=models.CharField(max_length=3, verbose_name=b'Maximo grado academico', choices=[(b'MSc', b'MSc'), (b'PhD', b'PhD')]),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='max_grado_year',
            field=models.IntegerField(verbose_name=b'A\xc3\xb1o de obtencion', choices=[(1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)]),
        ),
    ]
