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
        # 이 세 개의 매개 변 수 를 판단 하여 적합 한 번역 기능 을 호출 하 다.
        result = main(text, type, is_confirm)
        # 여기 서 실 현 된 번역 기능 을 호출 하여 번역 할텍스트 를 번역 한 다음 에 되 돌려 주 는 것 입 니 다.
        context = {
            'status': 200,
            'result': result
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return render(request, "index.html")


def test(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        type = request.POST.get('type')
        is_confirm = request.POST.get('is_confirm')
        # 이 세 개의 매개 변 수 를 판단 하여 적합 한 번역 기능 을 호출 하 다.
        result = main.main(text, type, is_confirm)
        # 여기 서 실 현 된 번역 기능 을 호출 하여 번역 할텍스트 를 번역 한 다음 에 되 돌려 주 는 것 입 니 다.
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
