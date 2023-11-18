# Generated by Django 4.2 on 2023-10-30 09:28

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateField(default=datetime.date(2023, 10, 30)),
        ),
        migrations.AlterField(
            model_name="post",
            name="img",
            field=models.ImageField(default="", null=True, upload_to="images_uploaded"),
        ),
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 10, 30, 9, 28, 35, 605111, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="video",
            field=models.FileField(
                default="",
                null=True,
                upload_to="videos_uploaded",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv", "gif"]
                    )
                ],
            ),
        ),
    ]
