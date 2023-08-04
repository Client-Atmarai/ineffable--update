# Generated by Django 4.2.3 on 2023-07-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ineffable_app", "0034_delete_unknown"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student_form_creation",
            fields=[
                ("name", models.CharField(max_length=20)),
                ("rollno", models.AutoField(primary_key=True, serialize=False)),
                ("image", models.ImageField(upload_to="")),
                ("dob", models.CharField(max_length=10)),
                ("course_name", models.CharField(max_length=150)),
                ("session", models.CharField(max_length=30)),
                ("percnt", models.IntegerField()),
                ("grade", models.CharField(max_length=30)),
                ("centre_code", models.IntegerField()),
                ("remark", models.CharField(max_length=10)),
                ("sub1", models.IntegerField()),
                ("sub2", models.IntegerField()),
                ("sub3", models.IntegerField()),
                ("sub4", models.IntegerField()),
                ("sub5", models.IntegerField()),
                ("wm", models.IntegerField()),
                ("pm", models.IntegerField()),
                ("am", models.IntegerField()),
                ("vm", models.IntegerField()),
            ],
        ),
    ]