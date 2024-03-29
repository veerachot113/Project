# Generated by Django 4.2.9 on 2024-02-13 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0023_alter_userdriver_groups_and_more"),
        ("driver", "0008_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="vehicles/")),
                ("model", models.CharField(max_length=100)),
                (
                    "type",
                    models.CharField(
                        choices=[("Sack", "แบบรองกระสอบ"), ("Bucket", "แบบถังอุ้ม")],
                        max_length=10,
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("province", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.userdriver",
                    ),
                ),
            ],
        ),
    ]
