# Generated by Django 3.0.8 on 2021-04-23 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20210401_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='Our_Values2',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
