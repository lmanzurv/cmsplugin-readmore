# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_readmore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readmore',
            name='append_icon',
        ),
        migrations.RemoveField(
            model_name='readmore',
            name='prepend_icon',
        ),
        migrations.RemoveField(
            model_name='readmore',
            name='title',
        ),
        migrations.AddField(
            model_name='readmore',
            name='append_icon_closed',
            field=models.CharField(max_length=50, null=True, verbose_name='Appended Icon Class When Closed', blank=True),
        ),
        migrations.AddField(
            model_name='readmore',
            name='append_icon_open',
            field=models.CharField(max_length=50, null=True, verbose_name='Appended Icon Class When Open', blank=True),
        ),
        migrations.AddField(
            model_name='readmore',
            name='prepend_icon_closed',
            field=models.CharField(max_length=50, null=True, verbose_name='Prepended Icon Class When Closed', blank=True),
        ),
        migrations.AddField(
            model_name='readmore',
            name='prepend_icon_open',
            field=models.CharField(max_length=50, null=True, verbose_name='Prepended Icon Class When Open', blank=True),
        ),
        migrations.AddField(
            model_name='readmore',
            name='title_closed',
            field=models.CharField(default='Read more', max_length=250, verbose_name='Link Text When Closed'),
        ),
        migrations.AddField(
            model_name='readmore',
            name='title_open',
            field=models.CharField(default='Read less', max_length=250, null=True, verbose_name='Link Text When Open', blank=True),
        ),
    ]
