from django import forms
from .models import Socio, Entrenador, Clase


class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = "__all__"


class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = "__all__"


class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = "__all__"


class SearchForm(forms.Form):
    query = forms.CharField(label="Buscar", max_length=100)
    q = forms.CharField(
        label="Buscar socio",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Buscar socio'})
    )