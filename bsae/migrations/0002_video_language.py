# Generated by Django 4.1.7 on 2023-02-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bsae", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="language",
            field=models.CharField(
                choices=[
                    ("English", "English"),
                    ("Hindi", "Hindi"),
                    ("Tamil", "Tamil"),
                ],
                default="English",
                max_length=10,
            ),
        ),
    ]
