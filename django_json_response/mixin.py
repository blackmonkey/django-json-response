from django.core.serializers import serialize
from django.core.paginator import Page, Paginator
from django.db import models
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.views.generic.base import TemplateResponseMixin

import json


def queryset_to_dict(qs: QuerySet) -> list:
  data = json.loads(serialize('json', qs))
  # Move 'fields' items one layer up
  for item in data:
    item.update(item.pop('fields'))
  return data


class JsonResponseMixin(TemplateResponseMixin):
  """
  Mixin to typically override TemplateResponseMixin and convert the view's response to a JSON response.
  """

  template_name = None
  template_engine = None
  content_type = "application/json"

  def dispatch(self, request, *args, **kwargs):
    try:
      return super().dispatch(request, *args, **kwargs)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=500)

  def is_duplicate_result(self, key, value):
    if hasattr(self, 'get_context_object_name'):
      context_obj_name = self.get_context_object_name(value)
      return context_obj_name is not None and key == context_obj_name
    return False

  def render_to_response(self, context, **response_kwargs):
    """
    Return a JsonResponse.

    Pass response_kwargs to the constructor of the response class.
    """
    response_kwargs.setdefault("content_type", self.content_type)

    items_to_delete = ['view']

    # Iterate through items in context and check for QuerySets
    for key, value in context.items():
      if isinstance(value, QuerySet):
        # To here, the view should be a ListView, and the context contains two items whose values are equal.
        # Keep `object_list` while remove the other.
        if self.is_duplicate_result(key, value):
          items_to_delete.append(key)
        else:
          context[key] = queryset_to_dict(value)
      elif isinstance(value, Paginator):
        context[key] = {
          'object_count': value.count,
          'num_pages': value.num_pages
        }
      elif isinstance(value, Page):
        context[key] = {
          'object_list': queryset_to_dict(value.object_list),
          'page_number': value.number
        }
      elif isinstance(value, models.Model):
        # To here, the view should be a DetailView, and the context contains two items whols values are equal.
        # Keep `object` while remove the other.
        if self.is_duplicate_result(key, value):
          items_to_delete.append(key)
        else:
          objs = queryset_to_dict([value])
          context[key] = objs[0]

    for key in items_to_delete:
      del context[key]

    return JsonResponse(context, **response_kwargs)
