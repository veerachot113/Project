# Generated by Django 4.2.9 on 2024-02-13 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0023_alter_userdriver_groups_and_more"),
        ("driver", "0004_remove_jobschedule_car_rename_driver_car_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="accounts.userdriver",
                    ),
                ),
                ("address", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=15)),
                ("work_experience", models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name="Car",
        ),
    ]
