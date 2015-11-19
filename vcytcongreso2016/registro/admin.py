from django.contrib import admin
from models import Pais, Departamento
from models import Frascati_nivel, Frascati_categoria
from models import Investigador

class InvestigadorAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'telefono', 'genero', 'email', 'telefono')

admin.site.register(Pais)
admin.site.register(Departamento)

admin.site.register(Frascati_nivel)
admin.site.register(Frascati_categoria)

admin.site.register(Investigador, InvestigadorAdmin)


# user: admin
# email: arteagamarcelo@gmail.com
# pass: Vcyt123