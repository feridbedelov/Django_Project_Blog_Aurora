# Generated by Django 2.2.1 on 2019-06-04 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created',
        ),
        migrations.RemoveField(
            model_name='category',
            name='modified',
        ),
    ]
