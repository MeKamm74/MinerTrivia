# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0004_auto_20150114_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_id',
        ),
        migrations.AlterField(
            model_name='question',
            name='date_open',
            field=models.DateField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
