# Generated by Django 4.2 on 2023-05-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_rename_a_soutenue_doctorant_soutenu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorant',
            name='option',
            field=models.CharField(choices=[('SI', 'SI'), ('SIQ', 'SIQ')], max_length=100, null=True),
        ),
    ]
