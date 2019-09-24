# Generated by Django 2.2.1 on 2019-06-30 11:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0024_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='posts_watchlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='WishList',
        ),
    ]
