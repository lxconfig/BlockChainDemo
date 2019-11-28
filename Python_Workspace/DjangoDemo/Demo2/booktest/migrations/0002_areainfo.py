# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('area_name', models.CharField(max_length=30)),
                ('parent_name', models.ForeignKey(to='booktest.AreaInfo', null=True, blank=True)),
            ],
        ),
    ]
