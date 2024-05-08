# Generated by Django 4.2.6 on 2024-05-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("SalleDeSport", "0010_remove_seance_jours_delete_jour_seance_jours"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="seance",
            name="jours",
        ),
        migrations.AddField(
            model_name="seance",
            name="jour",
            field=models.CharField(
                choices=[
                    (0, "Lundi"),
                    (1, "Mardi"),
                    (2, "Mercredi"),
                    (3, "Jeudi"),
                    (4, "Vendredi"),
                    (5, "Samedi"),
                    (6, "Dimanche"),
                ],
                default="",
                max_length=12,
            ),
            preserve_default=False,
        ),
    ]