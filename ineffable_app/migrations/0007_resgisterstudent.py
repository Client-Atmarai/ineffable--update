# Generated by Django 4.2.1 on 2023-05-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ineffable_app', '0006_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResgisterStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('rollno', models.IntegerField()),
                ('dob', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=30)),
                ('mark1', models.IntegerField()),
                ('mark2', models.IntegerField()),
                ('mark3', models.IntegerField()),
                ('percentage', models.IntegerField()),
                ('address', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]
