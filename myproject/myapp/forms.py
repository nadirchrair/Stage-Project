from django import forms
from .models import *
class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ('faculté', 'nom', 'prenom', 'date_de_naissance', 'Grade','critérs','nombre_document',)
        widgets = {
            'faculté': forms.Select(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'date_de_naissance': forms.DateInput(attrs={'class': 'form-control'}),
            'Grade': forms.Select(attrs={'class': 'form-control'}),
            'critérs': forms.Select(attrs={'class': 'form-control'}),
            'nombre_document': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class DocumentForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file', 'multiple': True}))
