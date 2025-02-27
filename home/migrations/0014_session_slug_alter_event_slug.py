# Generated by Django 4.1.12 on 2023-10-07 12:32
from django.db import migrations
from django.db import models
from django.utils.text import slugify


def slugify_title(apps, schema_editor):
    Session = apps.get_model("home", "Session")
    for session in Session.objects.filter(slug__isnull=True):
        session.slug = slugify(session.title)
        session.save(update_fields=["slug"])


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0013_sessionmembership_unique_session_membership"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="slug",
            field=models.SlugField(
                help_text="This is used in the URL to identify the session.",
                null=True,
                unique=True,
            ),
        ),
        migrations.RunPython(slugify_title, migrations.RunPython.noop, elidable=True),
    ]
