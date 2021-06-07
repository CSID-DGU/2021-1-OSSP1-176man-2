from django.shortcuts import render
import os
from django.http import HttpResponse
import json
import main

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def trans(request):
    return render(request, "index.html")


def home(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        type = request.POST.get('type')
        is_confirm = request.POST.get('is_confirm')
        result = main(text, type, is_confirm)

        context = {
            'status': 200,
            'result': result
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return render(request, "index.html")


def trans(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        type = request.POST.get('type')
        is_confirm = request.POST.get('is_confirm')
        result = main.main(text, type, is_confirm)
        context = {
            'status': 200,
            'result': result
        }
    else:
        context = {
            'status': 403,
            'result': 'post 요청 만 접수！'
        }
    return HttpResponse(json.dumps(context), content_type="application/json")
