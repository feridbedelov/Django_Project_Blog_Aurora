# Generated by Django 2.2.1 on 2019-07-25 12:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts_watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
