# Generated by Django 3.0.8 on 2021-09-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Privacy_Text', models.TextField(max_length=1000)),
            ],
        ),
    ]