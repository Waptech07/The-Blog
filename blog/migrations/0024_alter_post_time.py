# Generated by Django 4.1.13 on 2023-11-09 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0023_alter_post_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 11, 9, 17, 34, 2, 292565, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]