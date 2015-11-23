from django import forms
from django.conf import settings
from django.forms import ModelForm
from models import Investigador

class InvestigadorForm(ModelForm):
    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Investigador
        fields = '__all__'