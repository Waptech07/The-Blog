# Generated by Django 4.1.13 on 2023-11-09 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0020_alter_post_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 11, 9, 14, 41, 45, 919235, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
