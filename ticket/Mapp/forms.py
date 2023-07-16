from django import forms
from Mapp.models import movie
class Mappform(forms.ModelForm):

    class Meta:
        model=movie
        fields='__all__'