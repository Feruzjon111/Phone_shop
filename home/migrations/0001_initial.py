# Generated by Django 5.1.7 on 2025-03-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("phone", models.CharField(max_length=9)),
                ("name", models.CharField(max_length=70)),
                ("email", models.EmailField(max_length=254)),
                ("text", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Comment",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="Phone",
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
                ("brand", models.CharField(max_length=70)),
                ("model", models.CharField(max_length=70)),
                ("color", models.CharField(max_length=70)),
                ("price", models.PositiveIntegerField()),
                ("description", models.TextField(blank=True, null=True)),
                ("is_sold", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("is_existence", models.BooleanField(default=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Phone",
                "ordering": ["-created_date"],
            },
        ),
    ]
