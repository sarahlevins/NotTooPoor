# Generated by Django 2.2.5 on 2019-09-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoorUsers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.FloatField(default='0'),
        ),
    ]
