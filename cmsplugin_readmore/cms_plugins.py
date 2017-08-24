# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from django.templatetags.static import static
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import ReadMore

class ReadMorePlugin(CMSPluginBase):
    model = ReadMore
    name = _('Read More')
    module = _('Generic')
    render_template = 'read_more.html'
    change_form_template = 'admin/read_more.html'
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': [
                'css_classes'
            ]
        }),
        (_('When Closed'), {
            'fields': [
                'title_closed',
                'prepend_icon_closed',
                'append_icon_closed'
            ]
        }),
        (_('When Open'), {
            'fields': [
                'title_open',
                'prepend_icon_open',
                'append_icon_open'
            ]
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(ReadMorePlugin, self).render(context, instance, placeholder)
        return context

    def icon_src(self, instance):
        return static('readmore/img/readmore.png')

    def icon_alt(self, instance):
        return '%s - %s' % (force_text(self.name), instance.title_closed)

plugin_pool.register_plugin(ReadMorePlugin)
