from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware import csrf
import json, os
from .model.book_test import Book



def hello(request):
    context  = {}
    context['hello'] = 'Hello World!'
    # return render(request, 'example.html', context)
    return render(request, 'test_vue.html')

def test_vue(request):
    return HttpResponse('戏说不是胡说')

def test_1(request):
    return render(request,'test_2.html')

# 由于不是直接使用jinja模板，需要另外获取csrf
# 在post之前需要先get一下来获取包含csrftoken的cookies
@ensure_csrf_cookie
def test_data_from_nodejs(request):
    if request.method == 'GET':
        print(request)
        result = {"title":"错误","data":"","city":"北京"}
        #json返回为中文，只要在ensure_csrf_cookie装饰时有返回就能获取csrf cookie
        # return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
        return redirect('http://localhost:8000/test/django/form')
    elif request.method == 'POST':
        print("in test_data_from_nodejs post")
        print(request)
        obj = request.FILES.get('avatar')
        if obj:
            file_path = os.path.join('static/QR_CODE', obj.name)
            with open(file_path, 'wb') as f:
                for line in obj.chunks():
                    f.write(line)
            # print(request.POST['message'])
            return HttpResponse('success')
        else:
            result = {"title":"错误","data":"123456"}
            return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")

# @ensure_csrf_cookie
def get_token(request):
    token = csrf.get_token(request)
    return JsonResponse({'token': token})