django-jsonschema-form
====================

This package renders a [jsonschema](http://json-schema.org/) as part of a django form.


# Installation

Just run ```pip install django-jsonschema-form``` and then add an entry on your django project's settings.

``` python

INSTALLED_APPS = [
    ...,
    jsonschemaform,
]

```

# How it works
The core component is basicaly a django widget that receives a jsonschema and renders a form fragment.
It uses the [JSON Editor](https://github.com/jdorn/json-editor) js library to actually render this fragment.

In practice you only have to override the admin widget like the snippet bellow.

``` python

# Imporing Widget
from jsonschemaform.admin.widgets.jsonschema_widget import JSONSchemaWidget

# Here it is used postgres JSONField field implementation. Other implementation can be used depending on your DB
from django.contrib.postgres.fields import JSONField

# JSONSchema definition
schema = {
    "title": "Config Schema",
    "description": "My configutation schema",
    "type": "object",
    "properties": {
        "columns": {
            "description": "List of columns size",
            "type": "array"
        },
        "class": {
            "description": "A reference css class",
            "type": "string"
        },
        "container": {
            "default": "container",
            "description": "Default page container",
            "type": "string"
        }
    },
    "required": [
        "columns",
    ],
}

# Overriding widgets for all instances of JSONField on PageAdmin form
class PageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONSchemaWidget(schema)}
    }

```
This form will look like

![rendered Jsonschema](/images/rendered.png)

### Usage in non-admin views

If you are using jsonschemaform in your regular django views, rather than in the django admin, you need to add a `{{ form.media }}` template variable to the `<head>` or end of the `<body>` HTML section of your templates.

``` html
<!DOCTYPE html>
<html>
<head>
  ...
  {{ form.media }}
</head>
<body>
...
</body>
</html>
```

The media variable is already added in default django admin templates.

# Tweaking the editor
It is possible to configure the editor through django settings using the key JSONSCHEMAFORM.

``` python
JSONSCHEMAFORM = {
    'css': {
        'all': (
            'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
        )
    },
    'options': {
        'theme': 'bootstrap3',
        'iconlib': 'bootstrap3',
        'no_additional_properties': True,
        'disable_collapse': True,
    }
}

```
The settings above is also the default configuration.

But you can override or add any options described on [JSON Editor options](https://github.com/jdorn/json-editor#options).
