# Generated by Django 5.0 on 2023-12-21 01:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0013_farmer_address_farmer_email_farmer_full_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="farmer",
            name="email",
        ),
    ]