# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0010_auto_20141211_0320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='productos',
        ),
        migrations.AddField(
            model_name='producto',
            name='categorias',
            field=models.ManyToManyField(to='miscelanea.Categoria'),
            preserve_default=True,
        ),
    ]
