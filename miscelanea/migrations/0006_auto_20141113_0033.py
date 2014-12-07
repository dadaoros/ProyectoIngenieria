# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0005_auto_20141113_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='productos',
            field=models.ManyToManyField(to='miscelanea.Producto'),
            preserve_default=True,
        ),
    ]
