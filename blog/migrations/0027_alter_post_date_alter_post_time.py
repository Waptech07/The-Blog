# Generated by Django 4.1.13 on 2023-11-11 04:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0026_alter_post_category_alter_post_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateField(default=datetime.date(2023, 11, 11)),
        ),
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 11, 11, 4, 27, 22, 641721, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]