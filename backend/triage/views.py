import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .rules import classify

MAX_DESCRIPTION_LENGTH = 500


@csrf_exempt
@require_POST
def triage(request):
    """Classify request data without saving or logging the user's description.

    The endpoint is exempt from CSRF because it has no accounts, cookies, or
    side effects. A future endpoint that stores data must restore CSRF checks.
    """
    try:
        payload = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Please send valid form data."}, status=400)

    scenario = payload.get("scenario", "")
    description = payload.get("description", "")
    if not isinstance(scenario, str) or not isinstance(description, str):
        return JsonResponse({"error": "Please check the form values."}, status=400)
    if len(description) > MAX_DESCRIPTION_LENGTH:
        return JsonResponse({"error": "Please keep your description to 500 characters or fewer."}, status=400)
    if not scenario and not description.strip():
        return JsonResponse({"error": "Choose a situation or write a short description."}, status=400)

    return JsonResponse({"result": classify(scenario, description)})
