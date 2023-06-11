from django import forms
from .models import *
class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = '__all__'
        exclude=('critérs','nombre_document')
        widgets = {
            'faculté': forms.Select(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'date_de_naissance': forms.DateInput(attrs={'class': 'form-control'}),
            'Grade': forms.Select(attrs={'class': 'form-control'}),
            #'critérs': forms.Select(attrs={'class': 'form-control'}),
            'payes_Destiné': forms.TextInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
            'labo_de_rechercher': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'dossier_construction': forms.FileInput(attrs={'class': 'form-control'}),
           # 'labo_de_rechercher': forms.TextInput(attrs={'class': 'form-control'}),

#            'nombre_document': forms.NumberInput(attrs={'class': 'form-control'}),
        }



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
            'observation': forms.Textarea(attrs={'class': 'form-control'}),
            'points': forms.NumberInput(attrs={'class': 'form-control'}),

        }
class CommissionForm(forms.ModelForm):
  class Meta:
        model = Commission
        fields = '__all__'
        exclude=('stage',)

        widgets = {
            'remarque': forms.Textarea(attrs={'class': 'form-control'}),
            'total_finale': forms.NumberInput(attrs={'class': 'form-control'}),

        }