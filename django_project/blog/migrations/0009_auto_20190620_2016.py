# Generated by Django 2.2.1 on 2019-06-20 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.FloatField(default=5.5, max_length=20),
        ),
    ]
