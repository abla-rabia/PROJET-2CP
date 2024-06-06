# Generated by Django 4.1.7 on 2023-03-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_rename_cs_pv_fichier_encadrant_laboratoire'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorant',
            name='statut',
            field=models.CharField(choices=[('Inscrit', 'Inscrit'), ('A soutenue', 'A soutenue'), ('Abondant', 'Abondant'), ('Radié', 'Radié')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='sexe',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True),
        ),
    ]
