# Generated by Django 2.0.2 on 2018-02-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_auto_20180205_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='born_at',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
