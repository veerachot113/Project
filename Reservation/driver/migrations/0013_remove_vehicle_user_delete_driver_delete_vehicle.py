# Generated by Django 4.2.9 on 2024-02-15 03:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("driver", "0012_driver_vehicle_delete_car"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicle",
            name="user",
        ),
        migrations.DeleteModel(
            name="Driver",
        ),
        migrations.DeleteModel(
            name="Vehicle",
        ),
    ]
