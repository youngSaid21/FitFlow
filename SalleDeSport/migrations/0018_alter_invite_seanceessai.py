# Generated by Django 4.2.6 on 2023-12-31 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("SalleDeSport", "0017_alter_instructeur_tel_alter_invite_tel_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invite",
            name="seanceEssai",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="SalleDeSport.seance",
                verbose_name="Séance d'essai",
            ),
        ),
    ]
