# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0003_auto_20141112_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='idPersona',
            field=models.BigIntegerField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producto',
            name='numeroReferencia',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='idProveedor',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
    ]
