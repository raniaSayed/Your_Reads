# Generated by Django 2.0.1 on 2018-02-05 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180205_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]