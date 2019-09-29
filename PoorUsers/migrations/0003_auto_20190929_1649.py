# Generated by Django 2.2.5 on 2019-09-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoorEvents', '0003_event_categories'),
        ('PoorUsers', '0002_customuser_favourite_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='favourite_categories',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favourite_categories',
            field=models.ManyToManyField(default='', to='PoorEvents.Category'),
        ),
    ]
