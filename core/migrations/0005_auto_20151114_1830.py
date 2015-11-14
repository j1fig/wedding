# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151114_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accomodation',
            name='address',
        ),
        migrations.AddField(
            model_name='accomodation',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='accomodation',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
