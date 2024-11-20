# Generated by Django 4.1.5 on 2023-12-11 04:42
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("wagtailcore", "0078_referenceindex"),
        ("home", "0016_session_application_end_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="GeneralPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
                ("body", wagtail.fields.RichTextField(blank=True, null=True)),
                ("date", models.DateTimeField(verbose_name="Post Date")),
                (
                    "content",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(
                                                class_name="heading-blog",
                                                max_length=255,
                                            ),
                                        )
                                    ],
                                    class_name="full",
                                ),
                            ),
                            ("subheading", wagtail.blocks.CharBlock(class_name="full")),
                            (
                                "paragraph",
                                wagtail.blocks.RichTextBlock(class_name="full"),
                            ),
                            ("HTML", wagtail.blocks.RawHTMLBlock(class_name="full")),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                            (
                                "text_with_heading",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(
                                                class_name="heading-blog",
                                                max_length=255,
                                            ),
                                        )
                                    ],
                                    class_name="full",
                                ),
                            ),
                            (
                                "text_heading_image",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(max_length=255),
                                        ),
                                        ("text", wagtail.blocks.TextBlock()),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                    ],
                                    class_name="full",
                                ),
                            ),
                            (
                                "video_embed",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(max_length=255),
                                        ),
                                        ("text", wagtail.blocks.TextBlock()),
                                    ],
                                    class_name="full",
                                ),
                            ),
                            (
                                "table",
                                wagtail.contrib.table_block.blocks.TableBlock(
                                    class_name="full"
                                ),
                            ),
                            (
                                "code_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "language",
                                            wagtail.blocks.ChoiceBlock(
                                                choices=[
                                                    ("Python", "python"),
                                                    ("Markup", "html"),
                                                    ("CSS", "css"),
                                                    ("Clojure", "clojure"),
                                                    ("Bash", "shell"),
                                                    ("Django", "django"),
                                                    ("Jinja2", "jinja2"),
                                                    ("Docker", "dockerfile"),
                                                    ("Git", "git"),
                                                    ("GraphQL", "graphql"),
                                                    ("Handlebars", "handlebars"),
                                                    (".ignore", "gitignore"),
                                                    ("JSON", "json"),
                                                    ("JSON5", "json5"),
                                                    ("Markdown", "md"),
                                                    ("Markdown", "md"),
                                                    ("React JSX", "jsx"),
                                                    ("React TSX", "tsx"),
                                                    ("SASS", "sass"),
                                                    ("SCSS", "scss"),
                                                    ("TypeScript", "ts"),
                                                    ("vim", "vim"),
                                                ]
                                            ),
                                        ),
                                        (
                                            "caption",
                                            wagtail.blocks.CharBlock(
                                                blank=True, max_length=255
                                            ),
                                        ),
                                        (
                                            "page",
                                            wagtail.blocks.CharBlock(
                                                blank=True, max_length=255
                                            ),
                                        ),
                                        (
                                            "code",
                                            wagtail.blocks.TextBlock(
                                                blank=True, max_length=1000
                                            ),
                                        ),
                                    ],
                                    class_name="full",
                                ),
                            ),
                            (
                                "quote_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "text",
                                            wagtail.blocks.CharBlock(max_length=255),
                                        ),
                                        (
                                            "attribution",
                                            wagtail.blocks.CharBlock(max_length=255),
                                        ),
                                    ],
                                    class_name="full",
                                ),
                            ),
                        ],
                        blank=True,
                        null=True,
                        use_json_field=None,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="GeneralTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="home.generalpage",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="generalpage",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="home.GeneralTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
