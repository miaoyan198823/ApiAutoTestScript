
from blog import forms
from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from blog import models
from django.db.models import Q
from django.db.models import Count


# Create your views here.

def register(request):
    if request.method == "GET":
        regForm = forms.RegForm()
        return render(request,"register.html",{"regForm":regForm})
    elif request.method == "POST":
        regForm = forms.RegForm(request.POST)
        ret = {"success_info": None, "error_info": None}
        if regForm.is_valid():
            username = regForm.cleaned_data.get("username")
            password = regForm.cleaned_data.get("password")
            regForm.cleaned_data.pop("ret_password")
            avatar_img = request.FILES.get("avatar")
            user_info = models.UserInfo.objects.create(**regForm.cleaned_data)
            if user_info:
                ret['success_info'] = username
        else:
            ret['error_info'] = regForm.errors
        return JsonResponse(ret)


def check_reg_username(request):
    if request.method == "GET":
        ret  = {"msg_info":None}
        username = request.GET.get("username")
        user_exeit = models.UserInfo.objects.filter(username=username).first()
        if user_exeit:
            ret["msg_info"] = "用户已存在！"
        return JsonResponse(ret)


def login(request):
    if request.method == "GET":
        loginForm = forms.LoginForm()
        return render(request,"login.html",{"loginForm":loginForm})
    elif request.method == "POST":
        remember = request.POST.get("remember")
        loginForm = forms.LoginForm(request.POST)
        ret = {"success_info":None,"error_info":None}
        if loginForm.is_valid():
            login_user = models.UserInfo.objects.filter(**loginForm.cleaned_data).first()
            if login_user:
                request.session['is_login'] = True
                request.session['user_id'] = login_user.id
                if not remember:
                    request.session.set_expiry(0)
                ret['success_info'] = loginForm.cleaned_data.get("username")
        else:
            ret['error_info'] = loginForm.errors
        return JsonResponse(ret)

def reset_password(request):
    '''
    密码重置功能
    :param request:
    :return:
    '''
    if request.method == "GET":
        r_From = forms.ResetPasswordForm()
        return render(request,"reset_password.html",{"r_Form":r_From})
    if request.method == "POST":
        r_From = forms.ResetPasswordForm(request.POST)
        ret = {"success_info":None,"error_info":None}
        if r_From.is_valid():
            user_name = r_From.cleaned_data.get("user_name")
            new_password = r_From.cleaned_data.get("new_password")
            # old_password = r_From.cleaned_data.get("old_password")
            r_From.cleaned_data.pop("old_password")
            u_user_info = models.UserInfo.objects.get(username=user_name)
            u_user_info.password = new_password
            u_user_info.save()
            ret['success_info'] = user_name
        else:
            ret['error_info'] = r_From.errors
        return JsonResponse(ret)



def check_reset_username(request):
    if request.method == "GET":
        ret = {"info": None}
        user_name = request.GET.get("user_name")
        user_name_exit = models.UserInfo.objects.filter(username=user_name).first()
        if not user_name_exit:
            ret['info'] = "请输入正确用户名！"
        return JsonResponse(ret)

def check_old_password(request):
    if request.method == "GET":
        ret = {"set_info":None}
        old_password = request.GET.get("old_password")
        old_password_exit = models.UserInfo.objects.filter(password=old_password).first()
        if not old_password_exit:
            ret["set_info"] = "请输入正确旧密码！"
        return JsonResponse(ret)

def check_login_username(request):
    if request.method == "GET":
        ret = {"login_info":None}
        l_username = request.GET.get("username")
        user_exit = models.UserInfo.objects.filter(username=l_username).first()
        if not user_exit:
            ret["login_info"] = "用户名错误,请重新输入!"
        return JsonResponse(ret)

def logout(request):
    request.session.flush()
    return redirect("/home/")



def home(request):
    article_list = models.Article.objects.all()
    paginator = Paginator(article_list,5)
    page = request.GET.get("page")
    try:
        if page:
            print(page)
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    user = request.session.get("user_id")
    user_obj = models.UserInfo.objects.filter(id=user).first()
    return render(request,"home.html",{"user_obj":user_obj,"article_list":article_list})

def acticle_search(request):
    if request.method == "POST":
        search_info = request.POST.get("search")
        if search_info:
            search_list = models.Article.objects.filter(Q(title__icontains=search_info) | Q(desc__icontains=search_info))
            search_count = models.Article.objects.filter(Q(title__icontains=search_info) | Q(desc__icontains=search_info)).count()
            return render(request,"home.html",{"search_list":search_list,"search_out":search_count})
    article_list = models.Article.objects.all()
    return render(request,"home.html",{"article_list":article_list})

# def ajax_search(request):
#     if request.method == "POST":
#         search_info = request.POST.get("search")
#         print(search_info)
#         if search_info:
#             search_info_count = models.Article.objects.filter(Q(title__icontains=search_info) | Q(desc__icontains=search_info)).count()
#             data = {"count":search_info_count}
#             return JsonResponse(data)


#个人博客页
def index(request,username):
        #通过url配置取得访问用户数据
    #取Userinfo表里把用户对象取出来
    user = models.UserInfo.objects.filter(username=username).first()
    if user:
        #通过UserInfo表关联Blog表，通过用户直接获取该用户站点信息
        blog = user.blog
    else:
        return HttpResponse("500!")
    # 查询当前用户的所有文章列表
    article_list = models.Article.objects.filter(user=user)
    #查询当前用户站点下的所有分类
    # category_list = models.Category.objects.filter(blog=blog)
    #利用分组查询统计当前站点分类下的文章数
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title","c")
    #统计当前站点下有哪一些标签,且按标签统计出文章数量
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title","c")
    #按日期归档
    date_list = models.Article.objects.filter(user=user).extra(
        select={"d":"date_format(create_time,'%%Y-%%m')"}
    ).values("d").annotate(c=Count("nid")).values("d","c")
    return render(request,"index.html",{"blog":blog,
                                        "article_list":article_list,
                                        "category_list": category_list,
                                        "tag_list":tag_list,
                                        "date_list":date_list})


def article_detail(request,username,pk):
    '''
    :param username: 访问文章归属用户
    :param pk: 访问文章的主键id值
    :return:
    '''

    user = models.UserInfo.objects.filter(username=username).first()
    if user:
        blog = user.blog
    else:
        return HttpResponse("404!")
    print("----------------------------")
    article_obj = models.Article.objects.filter(pk=pk).first()
    return render(request,"article_detail.html",{"article":article_obj,
                                                 "blog":blog
                                                 })


def classes_list(request):
    class_list = models.Classes.objects.all()
    return render(request,"classes_list.html",{"class_list":class_list})



def add_classes(request):
    if request.method == "GET":
        ac_form = forms.AddClassForm()
        return render(request,"add_classes.html",{"ac_form":ac_form})
    if request.method == "POST":
        ac_form = forms.AddClassForm(request.POST)
        ret = {"msg_info":None,"error_info":None}
        if ac_form.is_valid():
            print(ac_form.cleaned_data.get("name"))
            models.Classes.objects.create(**ac_form.cleaned_data)
            ret['msg_info'] = ac_form.cleaned_data.get("name")
        else:
            ret['error_info'] = ac_form.errors
        return JsonResponse(ret)


def edit_class(request,nid):
    if request.method == "GET":
        c_obj =models.Classes.objects.filter(nid=nid).first()
        ac_form = forms.AddClassForm(initial={"name":c_obj.name})
        return render(request,"edit_class.html",{"nid":nid,"ac_form":ac_form})
    elif request.method == "POST":
        ac_form = forms.AddClassForm(request.POST)
        ret = {"msg_info":None,"error_info":None}
        if ac_form.is_valid():
            print(ac_form.cleaned_data)
            models.Classes.objects.filter(nid=nid).update(**ac_form.cleaned_data)
            ret['msg_info'] = ac_form.cleaned_data.get("name")
        else:
            ret['error_info'] = ac_form.errors
        return JsonResponse(ret)


def del_class(request,nid):
    if request.method == "GET":
        del_class_obj = models.Classes.objects.filter(nid=nid)
        if del_class_obj:
            del_class_obj.delete()
        return redirect("/classes_list/")

def student_list(request):
    if request.method == "GET":
        student_list = models.Student.objects.all()
        return render(request,"student_list.html",{"student_list":student_list})

def add_student(request):
    if request.method == "GET":
        as_form = forms.AddStudentForm()
        return render(request,"add_student.html",{"as_form":as_form})
    elif request.method == "POST":
        ret = {"msg_info":None,"error_info":None}
        as_form = forms.AddStudentForm(request.POST)
        if as_form.is_valid():
            models.Student.objects.create(**as_form.cleaned_data)
            ret['msg_info'] = as_form.cleaned_data.get("name")
        else:
            ret['error_info'] = as_form.errors
        return JsonResponse(ret)

def edit_student(request,nid):
    if request.method == "GET":
        #得到一个列表数据,所以取列表第一个数据,用first()方法
        as_obj = models.Student.objects.filter(nid=nid).values("name","age","email","address","cls_id").first()
        #initial传入一个字典格式数据,回显要编辑的内容
        as_form = forms.AddStudentForm(initial=as_obj)
        return render(request,"edit_student.html",{"as_form":as_form,"nid":nid})
    elif request.method == "POST":
        ret = {"msg_info":None,"error_info":None}
        as_form = forms.AddStudentForm(request.POST)
        if as_form.is_valid():
            models.Student.objects.filter(nid=nid).update(**as_form.cleaned_data)
            ret['msg_info'] = as_form.cleaned_data.get("name")
        else:
            ret['error_info'] = as_form.errors
        return JsonResponse(ret)

def del_student(request,nid):
    if request.method == "GET":
        del_stu_obj = models.Student.objects.filter(nid=nid)
        print(del_stu_obj)
        if del_stu_obj:
            del_stu_obj.delete()
        return redirect("/student_list/")


def teacher_list(request):
    teacher_list = models.Teacher.objects.all()
    return render(request,"teacher_list.html",{"teacher_list":teacher_list})


def add_teacher(request):
    if request.method == "GET":
        at_form = forms.AddTeacher()
        return render(request,"add_teacher.html",{"at_form":at_form})
    elif request.method == "POST":
        ret = {"msg_info":None,"error_info":None}
        at_form = forms.AddTeacher(request.POST)
        if at_form.is_valid():
            models.Teacher.objects.create(**at_form.cleaned_data)
            ret['msg_info'] = at_form.cleaned_data.get("name")
        else:
            ret['error_info'] = at_form.errors
        return JsonResponse(ret)

def edit_teacher(request,nid):
    if request.method == "GET":
        at_obj = models.Teacher.objects.filter(nid=nid).values("name","age","email","address").first()
        at_form = forms.AddTeacher(initial=at_obj)
        return render(request,"edit_teacher.html",{"at_form":at_form,"nid":nid})
    elif request.method == "POST":
        at_form = forms.AddTeacher(request.POST)
        ret = {"msg_info":None,"error_info":None}
        if at_form.is_valid():
            models.Teacher.objects.filter(nid=nid).update(**at_form.cleaned_data)
            ret['msg_info'] = at_form.cleaned_data.get("name")
        else:
            ret['error_info'] = at_form.errors
        return JsonResponse(ret)

def del_teacher(request,nid):
    if request.method == "GET":
        at_obj = models.Teacher.objects.filter(nid=nid)
        print(at_obj)
        if at_obj:
            at_obj.delete()
        return redirect("/teacher_list/")