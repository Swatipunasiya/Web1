from django import forms
from.models import Mymodel
class My_forms(forms.ModelForm):
    class Meta:
        model= Mymodel
        fields='__all__'