# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-30 23:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brew_data', '0007_auto_20171025_0751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestion',
            old_name='replace_object_id',
            new_name='replaced_object_id',
        ),
        migrations.RenameField(
            model_name='suggestion',
            old_name='object_id',
            new_name='suggested_object_id',
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='submitted_by_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
