# Generated by Django 2.2.5 on 2019-09-29 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoorUsers', '0003_auto_20190929_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favourite_categories',
            field=models.ManyToManyField(blank=True, default='', to='PoorEvents.Category'),
        ),
    ]
