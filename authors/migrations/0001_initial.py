# Generated by Django 2.0.1 on 2018-02-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('author_nationality', models.CharField(max_length=100)),
                ('born_at', models.DateField(blank=True, null=True)),
                ('died_at', models.DateField(blank=True, null=True)),
                ('contacts', models.TextField(max_length=200)),
                ('bio', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
