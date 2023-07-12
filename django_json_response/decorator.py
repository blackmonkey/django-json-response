from functools import wraps
from django.http import JsonResponse

def json_response(func):
  """
  Decorator to convert the view's response to a JSON response.
  """
  @wraps(func)
  def wrapper(*args, **kwargs):
    try:
      response = func(*args, **kwargs)
      if isinstance(response, dict):
        return JsonResponse(response)
      return response
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=500)
  return wrapper
