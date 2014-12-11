# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0012_canasta_detalleventa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canasta',
            name='operario',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
