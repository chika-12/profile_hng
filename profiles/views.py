from django.shortcuts import render

from django.http import JsonResponse
from datetime import datetime, timezone
import requests
import logging

logger = logging.getLogger(__name__)

def profile_view(request):
  CAT_URL = "https://catfact.ninja/fact"
  FALL_BACK = "Cats are amazing creatures with mysterious habits."

  try:
    response = requests.get(CAT_URL, timeout=5)
    response.raise_for_status
    cat_fact = response.json().get("fact", FALL_BACK)
    status_code = 200
  except response.exceptions.RequestExceptions as e:
    logger.error(f"Cat Fact API error {e}")
    cat_fact = FALL_BACK
    status_code = 503

  data = {
    "status": "success",
    "user": {
      "email": "markworship001@gmail.com",
      "name": "Chika Mark",
      "stack": "Python/Django"
    },
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "fact": cat_fact
  }
  return JsonResponse(data, status=status_code, content_type="application/json")
