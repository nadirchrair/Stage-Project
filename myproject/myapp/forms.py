from django import forms
from .models import *
class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ('faculté', 'nom', 'prenom', 'date_de_naissance', 'Grade','nombre_document',)
        widgets = {
            'faculté': forms.Select(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'date_de_naissance': forms.DateInput(attrs={'class': 'form-control'}),
            'Grade': forms.Select(attrs={'class': 'form-control'}),
            #'critérs': forms.Select(attrs={'class': 'form-control'}),
            'nombre_document': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class DocumentForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file', 'multiple': True}))


class CritéresForm(forms.ModelForm):
    class Meta:
        model = Critéres
        fields = '__all__'
        widgets = {
            'nom_de_Grille': forms.Select(attrs={'class': 'form-control'}),
            'critérs': forms.Textarea(attrs={'class': 'form-control'}),
        }

class FacultéForm(forms.ModelForm):
  class Meta:
        model = Faculté
        fields = '__all__'
        widgets = {
            'nom_faculté': forms.TextInput(attrs={'class': 'form-control'}),
        }
