# Generated by Django 4.2.6 on 2024-01-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("SalleDeSport", "0023_alter_club_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="club",
            name="ville",
            field=models.CharField(
                choices=[
                    ("Ag", "Agadir"),
                    ("Ca", "Casablanca"),
                    ("Mar", "Marakech"),
                    ("Ra", "Rabat"),
                    ("Tg", "Tanger"),
                ],
                max_length=64,
                verbose_name="Ville",
            ),
        ),
    ]
