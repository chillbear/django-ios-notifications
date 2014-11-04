# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ios_notifications', '0003_notification_loc_payload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apnservice',
            name='passphrase',
            field=django_fields.fields.EncryptedCharField(help_text=b'Passphrase for the private key', max_length=101, null=True, blank=True),
            preserve_default=True,
        ),
    ]
