# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0004_auto_20141113_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreCategoria', models.CharField(max_length=50)),
                ('productos', models.ManyToManyField(to='miscelanea.Producto', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='direccionProveedor',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='nombreProveedor',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
