# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('noti_type', models.PositiveSmallIntegerField(default=1, choices=[(1, b'Full notification'), (2, b'Web only notification'), (3, b'Email only notification')])),
                ('creation_dt', models.DateTimeField(auto_now_add=True)),
                ('displayed', models.BooleanField(default=False)),
                ('email_sent', models.BooleanField(default=False)),
                ('delivery_response', models.TextField(blank=True)),
                ('user', models.ForeignKey(related_name='notifications', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
