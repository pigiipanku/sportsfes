from django.http import JsonResponse

from rest_framework.views import APIView

from .models import SportsfesItem
# Create your views here.


class View(APIView):

    def get(self, request):

        response = {
            "success": False,
            "Content-Type": "application/json"
        }

        all_items = SportsfesItem.objects.all()

        for item in all_items:
            item.delete()

        response['success'] = True

        return JsonResponse(response)