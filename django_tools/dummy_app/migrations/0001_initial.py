# Generated by Django 4.1.4 on 2022-12-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Animeviews",
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
                ("name", models.CharField(max_length=200)),
                ("episodes", models.IntegerField(default=12)),
                ("genre", models.CharField(default="Action", max_length=20)),
                ("rating", models.FloatField()),
            ],
        ),
    ]
