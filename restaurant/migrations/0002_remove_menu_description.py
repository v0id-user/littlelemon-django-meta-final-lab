# Generated by Django 5.1.5 on 2025-01-29 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menu",
            name="description",
        ),
    ]
