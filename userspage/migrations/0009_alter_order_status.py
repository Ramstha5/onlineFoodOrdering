# Generated by Django 4.2.2 on 2023-12-27 01:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userspage", "0008_alter_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Out for deliver", "Out of deliver"),
                    ("Delivered", "Delivered"),
                ],
                default="Pending",
                max_length=200,
            ),
        ),
    ]