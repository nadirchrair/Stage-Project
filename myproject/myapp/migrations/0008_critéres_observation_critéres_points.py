# Generated by Django 4.0.6 on 2023-05-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_critéres_nom_de_grille'),
    ]

    operations = [
        migrations.AddField(
            model_name='critéres',
            name='observation',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='critéres',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
