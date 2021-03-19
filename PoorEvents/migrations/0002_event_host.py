# Generated by Django 2.2.5 on 2019-09-28 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PoorEvents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]