# Generated by Django 4.1.13 on 2023-11-09 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0022_alter_post_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 11, 9, 17, 32, 43, 233883, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
