# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-31 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_readmore', '0004_auto_20160901_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readmore',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_readmore_readmore', serialize=False, to='cms.CMSPlugin'),
        ),
    ]