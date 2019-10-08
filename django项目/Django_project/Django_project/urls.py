"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.urls import re_path
from blog import views
from django.views.static import serve
from Django_project.settings import MEDIA_ROOT
from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register),
    path('check_reg_username/',views.check_reg_username),
    path('login/',views.login),
    path('reset_password/',views.reset_password),
    path('check_old_password/',views.check_old_password),
    path('check_reset_username/',views.check_reset_username),
    path('check_login_username/',views.check_login_username),
    path('logout/',views.logout),
    path('home/',views.home),
    path('search/',views.acticle_search),
    # path('ajax_search/',views.ajax_search),
    #media相关的路由
    re_path('media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    #将所有以blog开头的url都交给blog_urls去处理
    path('blog/',include(blog_urls)),
    path('classes_list/',views.classes_list),
    path('add_classes/',views.add_classes),
    re_path('edit_class/(\d+)/',views.edit_class),
    re_path('del_class/(\d+)/',views.del_class),
    path('add_student/',views.add_student),
    path('student_list/',views.student_list),
    re_path('edit_student/(\d+)/',views.edit_student),
    re_path('del_student/(\d+)/',views.del_student),
    path('teacher_list/',views.teacher_list),
    path('add_teacher/',views.add_teacher),
    re_path('edit_teacher/(\d+)/',views.edit_teacher),
    re_path('del_teacher/(\d+)/',views.del_teacher),
]
