# Generated by Django 2.0.1 on 2018-02-06 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readedlist',
            name='book',
        ),
        migrations.DeleteModel(
            name='ReadedList',
        ),
    ]
