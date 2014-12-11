# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0011_auto_20141211_0605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canasta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operario', models.OneToOneField(null=True, to='miscelanea.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(default=1)),
                ('canasta', models.ForeignKey(to='miscelanea.Canasta', null=True)),
                ('producto', models.ForeignKey(to='miscelanea.Producto', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
