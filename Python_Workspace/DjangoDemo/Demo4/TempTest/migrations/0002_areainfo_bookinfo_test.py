# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('TempTest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(default=1, verbose_name='状态', choices=[(0, '上线'), (1, '下线')])),
                ('details', tinymce.models.HTMLField(verbose_name='详情', blank=True)),
            ],
            options={
                'db_table': 'tests',
                'verbose_name': '富文本测试',
                'verbose_name_plural': '富文本测试',
            },
        ),
    ]
