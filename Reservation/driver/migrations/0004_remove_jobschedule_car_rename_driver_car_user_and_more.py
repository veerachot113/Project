# Generated by Django 4.2.9 on 2024-02-13 05:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("driver", "0003_auto_20240213_1226"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="jobschedule",
            name="car",
        ),
        migrations.RenameField(
            model_name="car",
            old_name="driver",
            new_name="user",
        ),
        migrations.AlterField(
            model_name="car",
            name="image",
            field=models.ImageField(upload_to="car_images/"),
        ),
        migrations.AlterField(
            model_name="car",
            name="type",
            field=models.CharField(
                choices=[("Sack", "แบบรองกระสอบ"), ("Bucket", "แบบถังอุ้ม")],
                max_length=10,
            ),
        ),
        migrations.DeleteModel(
            name="Booking",
        ),
        migrations.DeleteModel(
            name="JobSchedule",
        ),
    ]
