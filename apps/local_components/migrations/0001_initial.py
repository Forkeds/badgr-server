# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import jsonfield.fields
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BadgeClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('json', jsonfield.fields.JSONField()),
                ('criteria_text', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'uploads/badges', blank=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=255)),
                ('created_by', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Badge classes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BadgeInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('json', jsonfield.fields.JSONField()),
                ('email', models.EmailField(max_length=255)),
                ('image', models.ImageField(upload_to=b'uploads/badges', blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=255, editable=False)),
                ('revoked', models.BooleanField(default=False)),
                ('revocation_reason', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('badgeclass', models.ForeignKey(related_name='badgeinstances', on_delete=django.db.models.deletion.PROTECT, to='local_components.BadgeClass', null=True)),
                ('created_by', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issuer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('json', jsonfield.fields.JSONField()),
                ('image', models.ImageField(upload_to=b'uploads/issuers', blank=True)),
                ('name', models.CharField(max_length=1024)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=255)),
                ('created_by', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='badgeinstance',
            name='issuer',
            field=models.ForeignKey(to='local_components.Issuer', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='badgeinstance',
            name='recipient_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='badgeclass',
            name='issuer',
            field=models.ForeignKey(related_name='badgeclasses', on_delete=django.db.models.deletion.PROTECT, to='local_components.Issuer'),
            preserve_default=True,
        ),
    ]