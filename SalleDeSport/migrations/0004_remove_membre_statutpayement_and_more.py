# Generated by Django 4.2.6 on 2023-12-31 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("SalleDeSport", "0003_modepaiement_membre_modepaiement"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="membre",
            name="statutPayement",
        ),
        migrations.AlterField(
            model_name="membre",
            name="coursInscrits",
            field=models.ManyToManyField(
                null=True,
                related_name="membres",
                to="SalleDeSport.cours",
                verbose_name="Cours",
            ),
        ),
        migrations.AlterField(
            model_name="membre",
            name="dateRenouvellement",
            field=models.DateField(null=True, verbose_name="Date du Renouvellement"),
        ),
        migrations.AlterField(
            model_name="membre",
            name="seancesReserves",
            field=models.ManyToManyField(
                null=True,
                related_name="membres",
                to="SalleDeSport.seance",
                verbose_name="Séances resérvées",
            ),
        ),
    ]
