# Generated by Django 4.2.7 on 2023-12-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MyLibraryData", "0007_remove_adherent_codeadh_livre_codeauteur"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adherent",
            name="nbrEmpruntAdh",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
