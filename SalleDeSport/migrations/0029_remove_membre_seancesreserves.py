# Generated by Django 4.2.6 on 2024-01-27 01:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("SalleDeSport", "0028_rename_reservationcours_reservationcour"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="membre",
            name="seancesReserves",
        ),
    ]
