from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def get_data(request):
    return JsonResponse({"status": "ok"}, status=200)

