# Generated by Django 5.0 on 2023-12-21 06:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0018_userdriver_name_userfarmer_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdriver",
            name="address",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="userfarmer",
            name="address",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="userdriver",
            name="username",
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="userfarmer",
            name="username",
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
