# Generated by Django 5.0.2 on 2024-02-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_rescuecontact_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="rescuecontact",
            name="phone_number",
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]
