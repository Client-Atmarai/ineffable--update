# Generated by Django 4.2.3 on 2023-07-30 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ineffable_app", "0039_add_centres_add_students"),
    ]

    operations = [
        migrations.RenameField(
            model_name="status_create",
            old_name="centre_name",
            new_name="centre_code",
        ),
    ]
