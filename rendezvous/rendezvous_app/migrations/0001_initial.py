# Generated by Django 5.0.3 on 2024-03-21 14:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("CountryID", models.IntegerField()),
                ("CountryName", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "countries",
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("TagID", models.IntegerField()),
                ("TagName", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("PostID", models.AutoField(primary_key=True, serialize=False)),
                ("Picture", models.ImageField(upload_to="")),
                ("Text", models.CharField(max_length=1000)),
                ("Upvotes", models.IntegerField(default=0)),
                ("Downvotes", models.IntegerField(default=0)),
                ("is_featured", models.BooleanField(default=False)),
                ("published_date", models.DateTimeField(auto_now_add=True)),
                (
                    "CountryID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="rendezvous_app.country",
                    ),
                ),
                (
                    "Tags",
                    models.ManyToManyField(
                        related_name="posts", to="rendezvous_app.tag"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("Picture", models.ImageField(blank=True, upload_to="profile_images")),
                ("Bio", models.CharField(max_length=500)),
                (
                    "BornInCountryID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="born_users",
                        to="rendezvous_app.country",
                    ),
                ),
                (
                    "LivingInCountryID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="living_users",
                        to="rendezvous_app.country",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("CommentID", models.AutoField(primary_key=True, serialize=False)),
                ("Content", models.CharField(max_length=280)),
                ("Upvotes", models.IntegerField()),
                ("Downvotes", models.IntegerField()),
                (
                    "PostID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="rendezvous_app.post",
                    ),
                ),
                (
                    "UserID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="rendezvous_app.user",
                    ),
                ),
            ],
        ),
    ]
