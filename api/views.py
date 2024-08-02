# api/views.py

from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

class ChatView(TemplateView):
    template_name = 'api/chat.html'

@csrf_exempt
def rasa_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            response = requests.post('http://localhost:5005/webhooks/rest/webhook', json=data)
            return JsonResponse(response.json(), safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)
