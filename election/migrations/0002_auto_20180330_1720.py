# Generated by Django 2.0 on 2018-03-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='started',
            field=models.BooleanField(default=True),
        ),
    ]
