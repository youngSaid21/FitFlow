# Generated by Django 4.2.6 on 2023-12-31 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("SalleDeSport", "0012_cours_activite_cours_instructeur"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cours",
            name="activite",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="SalleDeSport.activite",
                verbose_name="Activité",
            ),
        ),
        migrations.AlterField(
            model_name="cours",
            name="instructeur",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="SalleDeSport.instructeur",
                verbose_name="Instructeur",
            ),
        ),
    ]