# Generated by Django 4.2.6 on 2023-12-31 23:15

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("SalleDeSport", "0016_invite_seanceessai"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instructeur",
            name="tel",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None, unique=True, verbose_name="Téléphone"
            ),
        ),
        migrations.AlterField(
            model_name="invite",
            name="tel",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None, unique=True, verbose_name="Téléphone"
            ),
        ),
        migrations.AlterField(
            model_name="membre",
            name="tel",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None, unique=True, verbose_name="Téléphone"
            ),
        ),
    ]