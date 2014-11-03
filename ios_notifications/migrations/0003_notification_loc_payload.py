# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios_notifications', '0002_notification_silent'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='loc_payload',
            field=models.CharField(default='', help_text=b'JSON representation of an object containing the localization payload.', max_length=240, blank=True),
            preserve_default=False,
        ),
    ]
