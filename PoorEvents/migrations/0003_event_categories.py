# Generated by Django 2.2.5 on 2019-09-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoorEvents', '0002_event_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='categories',
            field=models.ManyToManyField(default='', to='PoorEvents.Category'),
        ),
    ]
