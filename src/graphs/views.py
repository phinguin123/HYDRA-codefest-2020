from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

def map_view(request, *args, **kwargs):
        return render(request, 'maps.html', {})

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels        = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
        default_items = [1, 1, 2, 1, 2, 2,3,5,2,4, 2,2,1,2,3,3,4,5,4,5,5,2,3,2,1]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)



def home_view(request, *args, **kwargs):
	return render(request, 'graphs/home.html', {})