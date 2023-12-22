# Generated by Django 5.0 on 2023-12-21 00:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0012_rename_userprofile_farmer"),
    ]

    operations = [
        migrations.AddField(
            model_name="farmer",
            name="address",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="farmer",
            name="email",
            field=models.EmailField(default="", max_length=254),
        ),
        migrations.AddField(
            model_name="farmer",
            name="full_name",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="farmer",
            name="phone",
            field=models.CharField(default="", max_length=15),
        ),
    ]
