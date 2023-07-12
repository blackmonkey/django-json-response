# Django JSON Response

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Build Status](https://github.com/blackmonkey/django-json-response/actions/workflows/django.yml/badge.svg)](https://github.com/blackmonkey/django-json-response/actions/workflows/django.yml)
[![Coverage Status](https://coveralls.io/repos/github/blackmonkey/django-json-response/badge.svg?branch=main)](https://coveralls.io/github/blackmonkey/django-json-response?branch=main)
[![Pypi version](https://img.shields.io/pypi/v/DjangoRestless)](https://pypi.org/project/DjangoRestless/)

Django JSON Response is a lightweight Django extension library that provides functionality to convert Django views' responses to JSON format, including both successful and failed responses. This library simplifies the process of serializing and formatting response data in JSON, making it easier to build APIs or handle AJAX requests in Django applications.

## Features
- Convert Django views' responses to JSON format.
- Handle successful responses and error responses with appropriate status codes.
- Flexible customization options for JSON serialization and formatting.

## Installation
Install Django JSON Response using pip:

```shell
pip install django-json-response
```

## Usage
Add `'django_json_response'` to your Django project's `INSTALLED_APPS` setting in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_json_response',
    ...
]
```

In your Django views, use the `json_response` decorator to wrap your view functions or class-based views. It will convert the view's response to JSON format:

```python
from django_json_response.decorators import json_response

@json_response
def my_view(request):
    # Your view logic here
    return {'key': 'value'}
```

You can also use the `JsonResponseMixin` in your class-based views to automatically convert the response to JSON:

```python
from django_json_response.mixins import JsonResponseMixin
from django.views.generic import View

class MyView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        # Your view logic here
        return {'key': 'value'}
```

For more advanced usage and customization options, please refer to the [documentation](https://img.shields.io/pypi/v/DjangoRestless).

## Contributing
Contributions are welcome! If you find any issues, have suggestions, or want to contribute to the project, please follow our [contribution guidelines](https://img.shields.io/pypi/v/DjangoRestless).

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/blackmonkey/django-json-response/blob/main/LICENSE) file for details.

Feel free to modify the content based on your specific requirements, adding more details, examples, or links to relevant resources.
