# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0002_alumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='maestros',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Identidad', models.CharField(max_length=15)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fechaNac', models.DateField()),
                ('sexo', models.ForeignKey(blank=True, to='alumno.sexo', null=True)),
            ],
        ),
    ]
