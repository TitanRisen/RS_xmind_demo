from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from ..model.materialForm import MaterialForm
from ..utils.create_xmind import gen_my_xmind_file
import json, os, uuid, base64, re
from config import img_file_path
import pymongo
# 接口参数表格路径
from ..api_table.post_get_material_api import material_table
# api_config_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/") + "../../api_table.json"

@ensure_csrf_cookie
def post_material_form(request):
    if request.method == 'POST':
        # with open(api_config_path, encoding='utf-8') as f:
        #     api_config=json.load(f) 
        req_from_json = {}
        for i in request:
            # 只取第一个元素
            req_from_json = json.loads(i)
            break
            
        ctx_db = dict()
        ctx_xmind = dict()
        file_list=[]
        # 所有非文件类都为必填项目
        # 处理request
        for item in material_table:
            if item['type'] == 'file':
                # obj = request.FILES.get(item['name'])
                # 改为用 base64 解码
                obj_b64 = req_from_json.get(item['name'])
                if obj_b64 :
                    # obj = base64.b64decode(obj_b64)
                    # nid = str(uuid.uuid4())
                    # file_path = os.path.join(img_file_path, nid +'_'+ '.png')
                    # with open(file_path, 'wb') as f:  # 把文件上传到已配置路径
                    #     #for line in obj.chunks():
                    #     f.write(obj)
                    # 1、信息提取
                    result = re.search("data:image/(?P<ext>.*?);base64,(?P<data>.*)", obj_b64, re.DOTALL)
                    if result:
                        ext = result.groupdict().get("ext")
                        data = result.groupdict().get("data")
                    else:
                        raise Exception("Do not parse!")
                    # 2、base64解码
                    img = base64.urlsafe_b64decode(data)
                    # 3、二进制文件保存
                    file_path = os.path.join(img_file_path, "{}.{}".format(uuid.uuid4(), ext))
                    with open(file_path, "wb") as f:
                        f.write(img)
                    file_list.append({'id': item['name'], 'name': item['title'], 'path':file_path } )
                    name = item['name'] + '_path'
                    ctx_db[ name ] = file_path

            elif item['type'] == 'number':
                obj = req_from_json.get(item['name'])
                if obj:
                    number = int(obj)
                    ctx_db[item['name']] = number

            elif item['type'] == 'array':
                obj = req_from_json.get(item['name'])
                if obj:
                    # print(item['name'])
                    # print(obj)
                    # 过滤空值
                    ctx_db[item['name']] = list(filter(None,obj))


            else:
                obj = req_from_json.get(item['name'])
                if req_from_json.get(item['name']):
                    ctx_db[item['name']] = obj
            # 如果存在必须要填但没填写的项目
            if item['required'] == True and not req_from_json.get(item['name']):
                message = item['name'] + "，该项需要填写"
                print(message)
                return HttpResponse(message, status=400)
        
        # 数据库操作
        try:
            MaterialForm.objects.create(**ctx_db)
            #    =======还需进行xmind的写入==============
            gen_my_xmind_file(ctx_db['item_name'] ,ctx_db, material_table, file_list)

        except pymongo.errors.DuplicateKeyError:
            print(pymongo.errors.DuplicateKeyError)
            return HttpResponse("已存在该项目", status=500)
        # except Exception:
        #     print("填写有误", Exception)
        #     return HttpResponse("填写有误", status=500)

        return HttpResponse("ok", status=200)

    elif request.method == 'GET':
        # return HttpResponse('ok')
        return redirect('http://localhost:8000/test/post_material_form') 


# 获取相关材料
def get_material_form(request, item_code):
    if request.method == 'GET':
        try:
            form = MaterialForm.objects(item_code = item_code)
            if not form or len(form) < 1:
                return HttpResponse("暂无该项目", status=400)
            form = form[0] # 暂时只取第一个结果

            res = dict()
            for key in form:
                if key[-4:] == "path":
                    file_path = form[key]
                    with open(file_path, 'r+') as f:
                        img_raw_data = f.read()
                        img_b64_string = base64.b64encode(img_raw_data)
                        name = key[:-5]  #去掉 _path
                        res[name] = img_b64_string
                else:
                    res[key] = form[key]
            res = json.dumps(res, ensure_ascii=False)
            print(res['item_name'])
            # 返回给前端
            return HttpResponse(res, content_type="application/json,charset=utf-8")

        except Exception:
            print(Exception)
            return HttpResponse("暂无该项目", status=50)
        
    