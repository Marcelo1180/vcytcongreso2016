from django import forms
from django.conf import settings
from models import Investigador

class InvestigadorForm(forms.Form):
    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Investigador