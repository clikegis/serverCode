# Generated by Django 4.1.2 on 2022-11-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0010_dataset_model_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataset",
            name="size",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
