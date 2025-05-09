# Generated by Django 5.0 on 2025-05-02 16:25

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("service", "0002_product_prod_head"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="prod_Shinfo",
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name="product",
            name="prod_benefit",
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name="product",
            name="prod_desc",
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name="product",
            name="prod_howtouse",
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name="product",
            name="prod_imptips",
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name="product",
            name="prod_nutinfo",
            field=tinymce.models.HTMLField(),
        ),
    ]
