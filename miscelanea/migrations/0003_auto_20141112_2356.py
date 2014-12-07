# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0002_persona_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numeroReferencia', models.IntegerField()),
                ('nombreProducto', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=30, blank=True)),
                ('existencias', models.IntegerField(default=0)),
                ('existenciaMinima', models.IntegerField(default=0)),
                ('descripcion', models.TextField(default=b'Sin descripcion')),
                ('precio', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idProveedor', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(to='miscelanea.Proveedor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
    ]
