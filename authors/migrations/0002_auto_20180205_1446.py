# Generated by Django 2.0.2 on 2018-02-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='author_nationality',
            field=models.CharField(default='string', max_length=100),
        ),
        migrations.AddField(
            model_name='authors',
            name='bio',
            field=models.CharField(default='string', max_length=200),
        ),
        migrations.AddField(
            model_name='authors',
            name='contacts',
            field=models.CharField(default='string', max_length=200),
        ),
        migrations.AlterField(
            model_name='authors',
            name='author_name',
            field=models.CharField(default='string', max_length=100),
        ),
    ]
