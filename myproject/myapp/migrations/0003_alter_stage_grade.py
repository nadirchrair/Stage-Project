# Generated by Django 4.0.6 on 2023-05-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_critéres_alter_stage_grade_alter_stage_nom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='Grade',
            field=models.CharField(choices=[('Professeur', 'Professeur'), ('Maitre de conférences - classe A', 'Maitre de conférences - classe A'), ('Doctoras Régime LMD', 'Doctoras Régime LMD')], max_length=100),
        ),
    ]
