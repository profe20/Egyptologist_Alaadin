# Generated by Django 3.2.10 on 2022-05-04 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0006_featuretours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toursbook',
            name='guest',
        ),
    ]
