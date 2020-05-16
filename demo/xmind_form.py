from django.http import HttpResponse
from django.shortcuts import render_to_response
from .utils.create_xmind import gen_my_xmind_file
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.cache import cache_page

import json

config_path="./config.json"  # 考虑用绝对路径或数据库

def search_form(request):
    return render_to_response('example_form.html')
 
def create_xmind(request):  
    # 改为从json文件读取配置
    request.encoding='utf-8'
    ctx = {}
    with open(config_path, encoding='utf-8') as f:
        config=json.load(f)
    ctx["form_items"] = config["form_items"]
    if request and request.POST and 'name' in request.POST and request.POST['name']:
        message = request.POST['name'] + ',你已提交成功'
        # gen_my_xmind_file(request.POST['name'] , request.POST['number']  , 
        #         request.POST['address']  , request.POST['flow'] ) 
        
        gen_my_xmind_file(request.POST['name'], request.POST, config["form_items"])
        request.POST=None
    else:
        message = ''
    ctx['rlt'] = message
    
    return render(request, "variable_form.html", ctx)
    # return render(request, "example_form.html", ctx)

def create_xmind_with_variable(request):
    pass