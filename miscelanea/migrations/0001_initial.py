# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=30)),
                ('idPersona', models.BigIntegerField()),
                ('telefono', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
