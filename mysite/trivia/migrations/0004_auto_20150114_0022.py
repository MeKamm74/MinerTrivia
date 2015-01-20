# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0003_auto_20150114_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_open',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
