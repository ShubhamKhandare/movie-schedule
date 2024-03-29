# Generated by Django 4.2 on 2024-02-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_movie_schedule_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="thumbnail",
            field=models.URLField(
                default="https://picsum.photos/150/100",
                help_text="The thumbnail of the movie",
                max_length=1000,
            ),
            preserve_default=False,
        ),
    ]
