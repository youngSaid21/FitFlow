# Generated by Django 4.2.6 on 2024-05-02 20:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("SalleDeSport", "0003_typeabonnement_avantages_typeabonnement_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="modepaiement",
            name="address",
        ),
        migrations.RemoveField(
            model_name="modepaiement",
            name="typeCarte",
        ),
        migrations.AddField(
            model_name="modepaiement",
            name="titulaire",
            field=models.CharField(
                default="", max_length=32, verbose_name="Titulaire de la carte"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="modepaiement",
            name="dateExp",
            field=models.CharField(max_length=5, verbose_name="expiration"),
        ),
    ]