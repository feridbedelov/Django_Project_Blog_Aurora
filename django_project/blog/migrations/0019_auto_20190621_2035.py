# Generated by Django 2.2.1 on 2019-06-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190620_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
