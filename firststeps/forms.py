from home.models import Terms
from django import forms


class TermsForm(forms.ModelForm):
    class Meta:
        model = Terms
        fields = ['accepted']

