# Generated by Django 5.0b1 on 2024-02-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0005_modelwithgenericforeignkey"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="configurations",
            field=models.JSONField(default=dict),
        ),
    ]
