# Generated by Django 5.0 on 2023-12-20 18:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_customuser_delete_membership_delete_userprofile"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
