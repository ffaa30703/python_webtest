# Generated by Django 2.2 on 2019-07-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
