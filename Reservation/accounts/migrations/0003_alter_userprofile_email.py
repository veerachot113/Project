# Generated by Django 5.0 on 2023-12-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_membership_userprofile_delete_farmer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]