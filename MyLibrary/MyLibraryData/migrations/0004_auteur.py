# Generated by Django 4.2.7 on 2023-11-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "MyLibraryData",
            "0003_adherent_adresseadh_adherent_datenaissanceadh_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Auteur",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nomAuteur", models.CharField(max_length=30)),
                ("prenomAuteur", models.CharField(max_length=30)),
            ],
        ),
    ]
