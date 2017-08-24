# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadMore',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('css_classes', models.CharField(max_length=250, null=True, verbose_name='CSS Classes', blank=True)),
                ('title', models.CharField(default='Read more', max_length=250, verbose_name='Link Text')),
                ('prepend_icon', models.CharField(max_length=50, null=True, verbose_name='Prepended Icon Class', blank=True)),
                ('append_icon', models.CharField(max_length=50, null=True, verbose_name='Appended Icon Class', blank=True)),
            ],
            options={
                'verbose_name': 'Read more',
                'verbose_name_plural': 'Read More',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
