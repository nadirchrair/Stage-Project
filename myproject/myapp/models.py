from django.db import models

# Create your models here.
class Type(models.Model):
    nom_de_Grille= models.CharField(max_length=50)
    def __str__(self):
        return self.nom_de_Grille
    
    
class Critéres(models.Model):
    nom_de_Grille=models.ForeignKey(Type, on_delete=models.CASCADE)
    critérs= models.CharField(max_length=1000)
    observation = models.CharField(max_length=1000)
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.critérs} => {self.observation} "
    
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
    payes_Destiné=models.CharField(max_length=50)
    ville=models.CharField(max_length=50)
    labo_de_rechercher=models.CharField(max_length=200)
    critérs =models.ForeignKey(Critéres, on_delete=models.CASCADE)
    nombre_document = models.IntegerField()
    file = models.FileField(upload_to='documents/')
    dossier_construction = models.FileField(upload_to='dossier/')
    def __str__(self):
        return f"{self.nom} {self.prenom} // {self.critérs}"
    @property
    def total(self):
        return self.nombre_document * self.critérs.points
    
class Commission(models.Model):
    stage= models.ForeignKey(Stage, on_delete=models.CASCADE)
    total_finale = models.IntegerField(default=0)
    remarque = models.TextField()
    def __str__(self):
        return f"{self.stage} {self.total_finale}"
class Myfinal(models.Model):
    datetime_field = models.DateTimeField()