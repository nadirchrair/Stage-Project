from django.db import models

# Create your models here.
class Type(models.Model):
    nom_de_Grille= models.CharField(max_length=50)

    

    def __str__(self):
        return self.nom_de_Grille
class Critéres(models.Model):
    nom_de_Grille=models.ForeignKey(Type, on_delete=models.CASCADE)
    critérs= models.CharField(max_length=1000)
    def __str__(self):
        return self.critérs
class Faculté(models.Model):
    nom_faculté=models.CharField(max_length=50)
    def __str__(self):
        return self.nom_faculté
    
class Stage(models.Model):
    CHOICE_A = 'Professeur'
    CHOICE_B = 'Maitre de conférences - classe A'
    CHOICE_C = 'Doctoras Régime LMD'

    CHOICES = [
        (CHOICE_A, 'Professeur'),
        (CHOICE_B, 'Maitre de conférences - classe A'),
        (CHOICE_C, 'Doctoras Régime LMD'),
    ]
    faculté=models.ForeignKey(Faculté, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField()
    Grade = models.CharField(max_length=100,choices=CHOICES)
    critérs =models.ForeignKey(Critéres, on_delete=models.CASCADE)
    nombre_document = models.IntegerField()
    file = models.FileField(upload_to='documents/')
    def __str__(self):
        return self.nom