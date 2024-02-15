# Generated by Django 4.2.9 on 2024-02-15 05:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0002_alter_vehicle_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="type",
            field=models.CharField(
                choices=[
                    ("แบบรองกระสอบ", "แบบรองกระสอบ"),
                    ("แบบถังอุ้ม", "แบบถังอุ้ม"),
                ],
                max_length=100,
            ),
        ),
    ]
