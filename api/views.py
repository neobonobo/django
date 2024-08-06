# api/views.py
import json
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RasaChatBotView(APIView):
    def post(self, request, *args, **kwargs):
        user_message = request.data.get('message')
        if not user_message:
            return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Forward the message to Rasa
        rasa_response = requests.post(
            'http://localhost:5005/webhooks/rest/webhook',  # Rasa server URL
            json={"message": user_message, "sender": "user"}
        )

        if rasa_response.status_code != 200:
            return Response({'error': 'Failed to communicate with Rasa'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        rasa_response_data = rasa_response.json()

        # Extract the bot's response
        if rasa_response_data:
            bot_response = rasa_response_data[0].get('text', 'No response from bot')
        else:
            bot_response = 'No response from bot'

        return Response({'message': bot_response}, status=status.HTTP_200_OK)

