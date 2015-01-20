# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0005_auto_20150114_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='anwer_text',
            new_name='answer_text',
        ),
    ]
