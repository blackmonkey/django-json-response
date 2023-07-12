from django.http import JsonResponse


class JsonResponseMixin:
  """
  Mixin to convert the view's response to a JSON response.
  """
  def render_to_json_response(self, context, **response_kwargs):
    return JsonResponse(context, **response_kwargs)

  def dispatch(self, request, *args, **kwargs):
    try:
      response = super().dispatch(request, *args, **kwargs)
      if isinstance(response, dict):
        return self.render_to_json_response(response)
      return response
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=500)
