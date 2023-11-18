# Generated by Django 4.1.13 on 2023-11-10 07:19

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0024_alter_post_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="img",
            field=models.ImageField(default="", upload_to="projects_uploaded"),
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateField(default=datetime.date(2023, 11, 10)),
        ),
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 11, 10, 7, 19, 6, 966455, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="video",
            field=models.FileField(
                blank=True,
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
