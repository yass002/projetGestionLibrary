# Generated by Django 4.2.7 on 2023-11-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MyLibraryData", "0002_emprunt_livre_emprunt_livre"),
    ]

    operations = [
        migrations.AddField(
            model_name="adherent",
            name="adresseAdh",
            field=models.CharField(default="Iteam University", max_length=30),
        ),
        migrations.AddField(
            model_name="adherent",
            name="dateNaissanceAdh",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="adherent",
            name="emailAdh",
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
