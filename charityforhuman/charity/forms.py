from django import forms
from charity.models import Charity

class CharityForm(forms.ModelForm):

    class Meta:
        model=Charity
        fields="__all__"