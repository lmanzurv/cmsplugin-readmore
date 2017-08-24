# -*- coding: utf-8 -*-
from django.db import models
from cms.models.pluginmodel import CMSPlugin
from aldryn_bootstrap3.model_fields import Icon
from django.utils.translation import ugettext_lazy as _

class ReadMore(CMSPlugin):
    css_classes = models.CharField(max_length=250, verbose_name=_('CSS Classes'), null=True, blank=True)
    title_closed = models.CharField(max_length=250, verbose_name=_('Link Text'), default=_('Read more'))
    title_open = models.CharField(max_length=250, verbose_name=_('Link Text'), null=True, blank=True, default=_('Read less'))
    prepend_icon_closed = Icon()
    prepend_icon_open = Icon()
    append_icon_closed = Icon()
    append_icon_open = Icon()

    class Meta:
        verbose_name = _('Read more')
        verbose_name_plural = _('Read More')

    def __unicode__(self):
        return self.title_closed
