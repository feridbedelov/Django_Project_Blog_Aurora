# Generated by Django 2.2.1 on 2019-06-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190621_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]