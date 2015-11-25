from django import forms
from django.conf import settings
from django.forms import ModelForm
from models import Investigador

class InvestigadorForm(ModelForm):
    fecha_nacimiento = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    fecha_llegada = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    fecha_retorno = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    disponibilidad = forms.BooleanField(help_text='Marque aqui si dispone de tiempo para asistir al evento', required=False)
    class Meta:
        model = Investigador
        fields = '__all__'