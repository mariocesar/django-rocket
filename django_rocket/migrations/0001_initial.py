# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvitationToken',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(unique=True, max_length=12, blank=True)),
                ('token', models.CharField(unique=True, editable=False, max_length=40)),
                ('uses', models.PositiveIntegerField(null=True, help_text='Number of uses that this token will be enabled, set 1 if it will work just once,No value to make it always enabled', blank=True, default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=140, blank=True)),
                ('last_name', models.CharField(max_length=140, blank=True)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'subscribers',
                'ordering': ('-created',),
                'verbose_name': 'subscriber',
            },
            bases=(models.Model,),
        ),
    ]
