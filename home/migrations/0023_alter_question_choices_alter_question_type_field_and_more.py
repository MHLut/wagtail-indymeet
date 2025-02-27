# Generated by Django 4.1.13 on 2024-02-25 19:25
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0022_remove_signuppage_page_ptr_delete_signupfield_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="choices",
            field=models.TextField(
                blank=True,
                help_text="If type field is radio, select, or multi select, fill in the options separated by commas. Ex: Male, Female.<br/>If type field is rating, use a number such as 5.",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="type_field",
            field=models.CharField(
                choices=[
                    ("TEXT", "Text"),
                    ("NUMBER", "Number"),
                    ("DATE", "Date"),
                    ("RADIO", "Radio"),
                    ("SELECT", "Select"),
                    ("MULTI_SELECT", "Multi Select"),
                    ("TEXT_AREA", "Text Area"),
                    ("URL", "URL"),
                    ("EMAIL", "Email"),
                    ("RATING", "Rating"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="survey",
            name="session",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="home.session",
            ),
        ),
    ]
