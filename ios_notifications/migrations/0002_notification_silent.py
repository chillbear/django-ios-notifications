# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='silent',
            field=models.NullBooleanField(help_text=b'set True to send a silent notification'),
            preserve_default=True,
        ),
    ]
