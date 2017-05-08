from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe

from jsonschemaform.default_settings import settings as conf
from django.conf import settings

import json


conf.update(getattr(settings, 'JSONSCHEMAFORM', {}))


class JSONSchemaWidget(Widget):

    template_name = 'jsonschema_widget.html'

    def __init__(self, sch, attrs=None):
        attrs = attrs or {}
        self.schema = sch
        super(JSONSchemaWidget, self).__init__(attrs)

    def get_context(self, name, value, attrs=None):
        opt = conf.get('options')
        opt.update({'startval': json.loads(value)})
        return {
            'id': attrs.get('id'),
            'name': name,
            'context': json.dumps({
                'id': attrs.get('id'),
                'attrs': attrs,
                'schema': self.schema,
                'options': opt
            })
        }

    def render(self, name, value, attrs=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)

    class Media(object):
        js = (
            'js/jsonschema-form.js',
            'js/jsoneditor.min.js',
        )
        css = conf.get('css')
