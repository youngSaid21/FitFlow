# Generated by Django 4.2.6 on 2023-12-31 00:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("SalleDeSport", "0002_reservationcours_alter_seance_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ModePaiement",
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
                (
                    "typeCarte",
                    models.CharField(max_length=24, verbose_name="Type du Carte"),
                ),
                (
                    "numeroCarte",
                    models.PositiveIntegerField(verbose_name="Numéro de la carte"),
                ),
                ("dateExp", models.DateField(verbose_name="Date d'expiration")),
                ("cvc", models.PositiveIntegerField(verbose_name="CVC")),
                ("address", models.CharField(verbose_name="Adresse de facturation")),
            ],
            options={
                "verbose_name": "Mode de paiement",
                "verbose_name_plural": "Modes de paiement",
                "db_table": "modepaiment",
            },
        ),
    ]
