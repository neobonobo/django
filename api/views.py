from django.shortcuts import render
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

# Configure logging
logger = logging.getLogger(__name__)

def chat_view(request):
    return render(request, 'api/chat.html')

@csrf_exempt
def rasa_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            if not user_message:
                logger.error("No message provided in request")
                return JsonResponse({"error": "No message provided"}, status=400)

            rasa_url = "http://localhost:5005/webhooks/rest/webhook"
            response = requests.post(rasa_url, json={"sender": "user", "message": user_message})
            response.raise_for_status()
            rasa_response = response.json()

            logger.info("Rasa response: %s", rasa_response)
            return JsonResponse(rasa_response, safe=False)
        except json.JSONDecodeError:
            logger.error("Invalid JSON in request")
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except requests.exceptions.RequestException as e:
            logger.error("Error communicating with Rasa: %s", e)
            return JsonResponse({"error": str(e)}, status=500)

    logger.error("Invalid request method")
    return JsonResponse({"error": "Invalid request method"}, status=400)
@csrf_exempt
def conversation_history(request):
    if request.method == "GET":
        try:
            sender_id = request.GET.get("sender_id", "user")
            rasa_url = f"http://localhost:5005/conversations/{sender_id}/tracker"
            response = requests.get(rasa_url)
            response.raise_for_status()
            history = response.json()

            return JsonResponse(history, safe=False)
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)
