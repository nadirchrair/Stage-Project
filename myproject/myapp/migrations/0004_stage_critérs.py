# Generated by Django 4.0.6 on 2023-05-18 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_stage_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='critérs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.critéres'),
        ),
    ]
