from django.http import JsonResponse


def convert_to_json_response(data:dict, status:int=200) -> JsonResponse:
  """
  Converts the given data to a JSON response.

  Args:
    data (dict): The data to be converted.
    status (int): The HTTP status code for the response. Defaults to 200.

  Returns:
    JsonResponse: The JSON response object.
  """
  return JsonResponse(data, status=status)


def convert_error_to_json_response(error_message, status:int=400) -> JsonResponse:
  """
  Converts an error message to a JSON response.

  Args:
    error_message (str): The error message.
    status (int): The HTTP status code for the response. Defaults to 400.

  Returns:
    JsonResponse: The JSON response object.
  """
  data = {'error': error_message}
  return JsonResponse(data, status=status)


def convert_response_to_json(response, status:int=200) -> JsonResponse:
  """
  Converts a Django view's response to a JSON response.

  Args:
    response: The original response object.
    status (int): The HTTP status code for the response. Defaults to 200.

  Returns:
    JsonResponse: The JSON response object.
  """
  data = {'response': response}
  return JsonResponse(data, status=status)


def convert_form_errors_to_json(form) -> JsonResponse:
  """
  Converts form errors to a JSON response.

  Args:
    form (django.forms.Form): The form object.

  Returns:
    JsonResponse: The JSON response object.
  """
  errors = {field: form.errors[field] for field in form.errors}
  return JsonResponse({'errors': errors}, status=400)
