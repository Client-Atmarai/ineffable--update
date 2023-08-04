# Generated by Django 4.2.3 on 2023-07-31 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ineffable_app", "0042_alter_add_students_centre_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="add_students",
            name="centre_code",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="centre_Code",
                to="ineffable_app.add_centres",
            ),
        ),
    ]
