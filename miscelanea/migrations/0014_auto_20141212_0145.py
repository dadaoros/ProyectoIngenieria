# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0013_auto_20141211_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombreProducto',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
