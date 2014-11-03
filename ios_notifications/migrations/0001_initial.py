# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APNService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('hostname', models.CharField(max_length=255)),
                ('certificate', models.TextField()),
                ('private_key', models.TextField()),
                ('passphrase', django_fields.fields.EncryptedCharField(help_text=b'Passphrase for the private key', max_length=110, null=True, block_type=b'MODE_CBC', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=64)),
                ('is_active', models.BooleanField(default=True)),
                ('deactivated_at', models.DateTimeField(null=True, blank=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('last_notified_at', models.DateTimeField(null=True, blank=True)),
                ('platform', models.CharField(max_length=30, null=True, blank=True)),
                ('display', models.CharField(max_length=30, null=True, blank=True)),
                ('os_version', models.CharField(max_length=20, null=True, blank=True)),
                ('service', models.ForeignKey(to='ios_notifications.APNService')),
                ('users', models.ManyToManyField(related_name='ios_devices', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeedbackService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('hostname', models.CharField(max_length=255)),
                ('apn_service', models.ForeignKey(to='ios_notifications.APNService')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(help_text=b'Alert message to display to the user. Leave empty if no alert should be displayed to the user.', max_length=200, blank=True)),
                ('badge', models.PositiveIntegerField(help_text=b'New application icon badge number. Set to None if the badge number must not be changed.', null=True, blank=True)),
                ('sound', models.CharField(help_text=b'Name of the sound to play. Leave empty if no sound should be played.', max_length=30, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_sent_at', models.DateTimeField(null=True, blank=True)),
                ('custom_payload', models.CharField(help_text=b'JSON representation of an object containing custom payload.', max_length=240, blank=True)),
                ('service', models.ForeignKey(to='ios_notifications.APNService')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='feedbackservice',
            unique_together=set([('name', 'hostname')]),
        ),
        migrations.AlterUniqueTogether(
            name='device',
            unique_together=set([('token', 'service')]),
        ),
        migrations.AlterUniqueTogether(
            name='apnservice',
            unique_together=set([('name', 'hostname')]),
        ),
    ]
