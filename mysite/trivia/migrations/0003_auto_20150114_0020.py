# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_myuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_open',
            field=models.DateField(verbose_name='date'),
            preserve_default=True,
        ),
    ]
