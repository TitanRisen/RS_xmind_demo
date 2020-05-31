from django.http import HttpResponse
# from django.shortcuts import render_to_response
from .utils.create_xmind import gen_my_xmind_file
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.cache import cache_page
import uuid
import json

import os
# config_path="./config.json"  # 考虑用绝对路径或数据库
config_path= os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/") + "/config_xmind.json"

# def create_xmind(request):  
#     # 改为从json文件读取配置
#     request.encoding='utf-8'
#     ctx = {}
#     with open(config_path, encoding='utf-8') as f:
#         config=json.load(f)
#     ctx["form_items"] = config["form_items"]
#     if request and request.POST and 'name' in request.POST and request.POST['name']:
#         message = request.POST['name'] + ',你已提交成功'
#         # gen_my_xmind_file(request.POST['name'] , request.POST['number']  , 
#         #         request.POST['address']  , request.POST['flow'] ) 
#         gen_my_xmind_file(request.POST['name'], request.POST, config["form_items"])
#         request.POST=None
#     else:
#         message = ''
#     ctx['rlt'] = message
    
#     return render(request, "variable_form.html", ctx)

def create_xmind(request):
    ctx = {}
    if request.method == 'GET':
        ctx = {
            'succeed': False,
            'script':"alert",
            'message':"无"
        }
        return render(request, "demo.html", ctx)
    elif request.method == 'POST':
        
        if not ('item_name' in request.POST and request.POST['item_name'] ):
            ctx = {
            'succeed': True,
            'script':"alert",
            'message':"注意：事项名称为必填项目"
            }
            return render(request, "demo.html" , ctx)

        #导入表单配置
        with open(config_path, encoding='utf-8') as f:
            config=json.load(f)

        # 单独处理图片
        file_list=[]
        for item in config["form_items"]:
            
            if item['type'] == 'photo':
                obj = request.FILES.get(item['id'])
                if not obj:     #如果该文件未上传就continue
                    continue
                nid = str(uuid.uuid4())  # 加一个随机码防止上传的文件重名
                # ret = {'status': True, 'data': None, 'message': None}
                # 把上传来的文件路径传给前端，让前端访问来显示上传的图片以达到预览的效果
                # ret['data'] = file_path
                file_path = os.path.join('static/QR_CODE', nid + obj.name)
                with open(file_path, 'wb') as f:  # 把文件上传到静态文件夹下
                    for line in obj.chunks():
                        f.write(line)
                # file_dic[item['id']] = file_path
                file_list.append({'id': item['id'], 'name': item['name'], 'path':file_path } )


        
        gen_my_xmind_file(request.POST['item_name'], request.POST, config["form_items"], file_list)

        ctx = {
            'succeed': True,
            'script':"alert",
            'message':"已成功上传"
        }
        return render(request, "demo.html" , ctx)