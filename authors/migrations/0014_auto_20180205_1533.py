# Generated by Django 2.0.2 on 2018-02-05 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0013_auto_20180205_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='born_at',
            field=models.DateField(null=True),
        ),
    ]
