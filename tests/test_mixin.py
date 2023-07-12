import json

from django.test import TestCase, RequestFactory
from django.views import View
from django_json_response import JsonResponseMixin

class SuccessView(JsonResponseMixin, View):
  def get(self, request, *args, **kwargs):
    response_data = {'message': 'Success!'}
    return response_data

class ErrorView(JsonResponseMixin, View):
  def get(self, request, *args, **kwargs):
    raise ValueError('Something went wrong.')

class JsonResponseMixinTestCase(TestCase):
  def setUp(self):
    self.factory = RequestFactory()

  def assert_response(self, response, status_code, content, content_type='application/json'):
    self.assertEqual(response.status_code, status_code)
    self.assertEqual(response.headers['content-type'], content_type)
    self.assertEqual(json.loads(response.content.decode()), content)

  def test_success_response(self):
    request = self.factory.get('/')
    view = SuccessView.as_view()
    response = view(request)
    self.assert_response(response, 200, {'message': 'Success!'})

  def test_error_response(self):
    request = self.factory.get('/')
    view = ErrorView.as_view()
    response = view(request)
    self.assert_response(response, 500, {'error': 'Something went wrong.'})
