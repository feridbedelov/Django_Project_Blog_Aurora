# Generated by Django 2.2.1 on 2019-06-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190620_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]