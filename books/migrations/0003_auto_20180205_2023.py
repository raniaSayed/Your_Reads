# Generated by Django 2.0.1 on 2018-02-05 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
