# Generated by Django 5.0.3 on 2024-03-22 18:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rendezvous_app", "0002_alter_comment_downvotes_alter_comment_upvotes"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="upvoted_by",
            field=models.ManyToManyField(
                blank=True, related_name="upvoted_comments", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
