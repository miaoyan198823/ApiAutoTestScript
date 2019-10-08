# -*- coding: utf-8 -*-
# @Time : 2019/6/3 10:31
# @Author : miaoyan


from django.urls import re_path
from blog import views

urlpatterns = [
    # path('up_down/',views.up_down),
    re_path('(\w+)/',views.index),
    re_path('(\w+)/article/(\d+)/',views.article_detail),#文章详情页

]