# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_readmore', '0002_auto_20160714_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readmore',
            name='append_icon_closed',
            field=models.CharField(max_length=50, null=True, verbose_name='Appended Icon Class', blank=True),
        ),
        migrations.AlterField(
            model_name='readmore',
            name='append_icon_open',
            field=models.CharField(max_length=50, null=True, verbose_name='Appended Icon Class', blank=True),
        ),
        migrations.AlterField(
            model_name='readmore',
            name='prepend_icon_closed',
            field=models.CharField(max_length=50, null=True, verbose_name='Prepended Icon Class', blank=True),
        ),
        migrations.AlterField(
            model_name='readmore',
            name='prepend_icon_open',
            field=models.CharField(max_length=50, null=True, verbose_name='Prepended Icon Class', blank=True),
        ),
        migrations.AlterField(
            model_name='readmore',
            name='title_closed',
            field=models.CharField(default='Read more', max_length=250, verbose_name='Link Text'),
        ),
        migrations.AlterField(
            model_name='readmore',
            name='title_open',
            field=models.CharField(default='Read less', max_length=250, null=True, verbose_name='Link Text', blank=True),
        ),
    ]
