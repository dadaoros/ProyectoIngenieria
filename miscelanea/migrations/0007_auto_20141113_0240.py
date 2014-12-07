# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0006_auto_20141113_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombreCategoria',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
