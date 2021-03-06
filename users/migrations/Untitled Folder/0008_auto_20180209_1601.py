# Generated by Django 2.0.2 on 2018-02-09 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0014_auto_20180207_2244'),
        ('users', '0007_ratelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNowList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='readedlist',
            name='published_at',
        ),
        migrations.AddField(
            model_name='readedlist',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
