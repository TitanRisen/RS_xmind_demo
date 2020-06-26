"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import view,xmind_form

from .controller.material_form_controller import post_material_form, get_material_form
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', view.hello),
    # url(r'^xmind$', xmind_form.search_form),
    url(r'^create_xmind$', xmind_form.create_xmind , name='create_xmind'),

    path('test/', view.test_1),
    path('test/data_django/', view.test_data_from_nodejs),
    path('test_1/', post_material_form),
    
    #提交表单，提交前先get一次csrftoken
    path('test/post_material_form', post_material_form),
    path('api/post/material_form', post_material_form),
    #获取表单
    path('api/get/material_form/<slug:item_code>/', get_material_form)
]
