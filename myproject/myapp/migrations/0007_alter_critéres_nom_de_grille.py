# Generated by Django 4.0.6 on 2023-05-18 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_type_critéres_nom_de_grille'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critéres',
            name='nom_de_Grille',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.type'),
        ),
    ]
