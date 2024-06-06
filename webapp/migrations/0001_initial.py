# Generated by Django 4.1.7 on 2023-03-12 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encadrant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('prénom', models.CharField(max_length=100, null=True)),
                ('telephone', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('etablissement', models.CharField(max_length=100, null=True)),
                ('grade', models.CharField(max_length=100, null=True)),
                ('interets', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numéro', models.CharField(max_length=100, null=True)),
                ('lien', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Séminaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, null=True)),
                ('type_seminaire', models.CharField(choices=[('Interne', 'Interne'), ('Externe', 'Externe')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctorant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('prénom', models.CharField(max_length=100, null=True)),
                ('date_de_naissance', models.DateField(null=True)),
                ('telephone', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('type_doc', models.CharField(choices=[('LMD', 'LMD'), ('Classique', 'Classique')], max_length=50, null=True)),
                ('option', models.CharField(max_length=100, null=True)),
                ('diplome', models.CharField(choices=[('Master', 'Master'), ('Magister', 'Magister'), ('Ingéniorat', 'Ingéniorat')], max_length=100, null=True)),
                ('etablissement_origine', models.CharField(max_length=100, null=True)),
                ('premiere_annee_inscription', models.CharField(max_length=100, null=True)),
                ('nbr_annees_inscription', models.IntegerField(null=True)),
                ('date_EFST', models.DateField(null=True)),
                ('laboratoire', models.CharField(max_length=100, null=True)),
                ('titre_these', models.CharField(max_length=300, null=True)),
                ('nv_titre', models.CharField(max_length=300, null=True)),
                ('date_soutenance', models.DateField(null=True)),
                ('observation', models.CharField(max_length=300, null=True)),
                ('a_soutenue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='soutenu', to='webapp.pv')),
                ('abondant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='abondant', to='webapp.pv')),
                ('co_directeur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='co_dir', to='webapp.encadrant')),
                ('directeur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.encadrant')),
                ('pv_changement_titre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='changement', to='webapp.pv')),
                ('radié', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='radié', to='webapp.pv')),
                ('tab_PVs', models.ManyToManyField(to='webapp.pv')),
                ('tab_séminaires', models.ManyToManyField(to='webapp.séminaire')),
            ],
        ),
    ]
