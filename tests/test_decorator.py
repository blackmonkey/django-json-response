import json

from django.http import HttpRequest
from django.test import TestCase
from django_json_response import json_response

@json_response
def success_view(request):
  return {'message': 'Success!'}

@json_response
def error_view(request):
  raise ValueError('Something went wrong.')

class JsonResponseDecoratorTestCase(TestCase):

  def assert_response(self, response, status_code, content, content_type='application/json'):
    self.assertEqual(response.status_code, status_code)
    self.assertEqual(response.headers['content-type'], content_type)
    self.assertEqual(json.loads(response.content.decode()), content)

  def test_success_response(self):
    request = HttpRequest()
    response = success_view(request)
    self.assert_response(response, 200, {'message': 'Success!'})

  def test_error_response(self):
    request = HttpRequest()
    response = error_view(request)
    self.assert_response(response, 500, {'error': 'Something went wrong.'})
