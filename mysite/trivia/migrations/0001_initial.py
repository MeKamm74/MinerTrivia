# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('question_text', models.CharField(max_length=200)),
                ('anwer_text', models.CharField(max_length=200)),
                ('question_id', models.IntegerField(default=0)),
                ('date_open', models.DateTimeField(verbose_name='date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
