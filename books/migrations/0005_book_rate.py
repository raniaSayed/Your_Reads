# Generated by Django 2.0.1 on 2018-02-05 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20180205_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rate',
            field=models.IntegerField(choices=[(1, 'SoBad'), (2, 'Bad'), (3, 'Normal'), (4, 'High'), (5, 'SoHigh')], default=1),
        ),
    ]