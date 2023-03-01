from home.models import Terms
from bank.models import Cards,Bank,CardBrand
from django import forms


class TermsForm(forms.ModelForm):
    class Meta:
        model = Terms
        fields = ['accepted']


class CardsForms(forms.ModelForm):
    class Meta:
        model = Cards
        fields = "__all__"


class BanckForms(forms.ModelForm):
    class Meta:
        model = Bank
        fields = "__all__"


class CardBrandFroms(forms.ModelForm):
    class Meta:
        model = CardBrand
        fields = "__all__"