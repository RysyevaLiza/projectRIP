# Generated by Django 4.1.2 on 2022-10-17 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="hotel",
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
                ("name", models.CharField(default=None, max_length=45)),
                ("address", models.CharField(default=None, max_length=45)),
                ("stars", models.CharField(default=None, max_length=3)),
                ("country", models.CharField(default=None, max_length=45)),
                ("image", models.ImageField(default=None, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="show",
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
                ("full_name", models.CharField(default=None, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="room",
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
                ("category", models.CharField(default=None, max_length=45)),
                ("max_count", models.IntegerField(blank=True, default=None, null=True)),
                ("bed_type", models.CharField(default=None, max_length=45)),
                ("price", models.IntegerField(blank=True, default=None, null=True)),
                ("total", models.IntegerField(blank=True, default=None, null=True)),
                (
                    "hotel_id",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hotel.hotel",
                    ),
                ),
            ],
        ),
    ]
