# -*- coding: utf-8 -*-
# @Time : 2019/5/27 14:27
# @Author : miaoyan

from django import forms
from django.forms import widgets
from blog import models
from django.core.exceptions import ValidationError



class RegForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="用户名:",
        required=True,
        widget=widgets.TextInput(
            attrs={
                'class':'form-control'
            }
        ),
        error_messages={
            'required': '用户名不能为空',
            'max_length': '最长是255',
        }
    )

    password = forms.CharField(
        max_length=16,
        min_length=3,
        label="密码:",
        required=True,
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={'max_length': '最长是255',
                        'min_length': '最短是3',
                        'required': '密码不能为空'
            }
    )

    ret_password = forms.CharField(
        max_length=255,
        min_length=3,
        label="确认密码:",
        required=True,
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={'max_length': '最长是255',
                        'min_length': '最短是3',
                        'required': '确认密码不能为空'
                        }
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        ret = models.UserInfo.objects.filter(username=username).first()
        if ret:
            raise ValueError("用户已存在！")
        return username


    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password.isdigit():
            raise ValidationError("密码不能是纯数字,请重新输入!")
        return password

    def clean(self):
        password = self.cleaned_data.get("password")
        ret_password = self.cleaned_data.get("ret_password")
        if ret_password and ret_password != password:
            self.add_error("ret_password",ValidationError("两次密码不一致!"))
        else:
            return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="用户名:",
        required=True,
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={
            'required': '用户名不能为空',
            'max_length': '最长是255',
        }

    )

    password = forms.CharField(
        max_length=255,
        min_length=3,
        label="密码:",
        required=True,
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={'max_length': '最长是255',
                        'min_length': '最短是3',
                        'required': '密码不能为空'
                        }

    )


    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        pwd_info = models.UserInfo.objects.filter(password=pwd).first()
        if not pwd_info:
            raise  ValidationError("密码错误,请重新输入!")
        return pwd

class ResetPasswordForm(forms.Form):
    user_name = forms.CharField(
        max_length=255,
        label="用户名:",
        required=True,
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={
            'required': '用户名不能为空',
            'max_length': '最长是255',
        }
    )

    old_password = forms.CharField(
        max_length=255,
        min_length=3,
        label="旧密码:",
        required=True,
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={'max_length': '最长是255',
                        'min_length': '最短是3',
                        'required': '旧密码不能为空'
                        }
    )

    new_password = forms.CharField(
        max_length=255,
        min_length=3,
        label="新密码:",
        required=True,
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={'max_length': '最长是255',
                        'min_length': '最短是3',
                        'required': '新密码不能为空'
                        }
    )


    def clean(self):
        old_password = self.cleaned_data.get("old_password")
        new_password = self.cleaned_data.get("new_password")
        if new_password and new_password == old_password:
            self.add_error("new_password",ValidationError("新密码不能与旧密码一致,请重新输入！"))
        return self.cleaned_data


    def clean_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        if new_password.isdigit():
            raise ValidationError("新密码不能为纯数字,请重新输入!")
        return new_password


class AddClassForm(forms.Form):
    name = forms.CharField(
        max_length=32,
        label="班级名称:",
        required=True,
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={
            'required': '班级名称不能为空!',
            'max_length': '最长是32',
        }
    )


class AddStudentForm(forms.Form):
    name = forms.CharField(
        max_length=32,
        label="姓名:",
        required=True,
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={
            'required': '姓名不能为空!',
            'max_length': '最长是32',
        }
    )


    age = forms.IntegerField(
        min_value=18,
        max_value=25,
        label="年龄:",
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': '年龄不能为空!',
        }
    )

    email = forms.EmailField(
        max_length=32,
        label="邮箱:",
        required=True,
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={
            'required': '邮箱不能为空!',
            'invalid': '邮箱格式错误!',
        }
    )

    address = forms.CharField(
        max_length=64,
        label="地址:",
        required=True,
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={
            'required': '地址不能为空!',
            'max_length': '最长是64',
        }

    )

    cls_id = forms.IntegerField(
        label="所属班级:",
        required = True,
        widget=widgets.Select(choices=models.Classes.objects.values_list("nid","name"),attrs={'class': 'form-control'}),
        error_messages={
            'required': '所属班级不能为空!',
        }
    )


class AddTeacher(forms.Form):
    name = forms.CharField(
        max_length=32,
        label="姓名:",
        required=True,
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={
            'required': '姓名不能为空!',
            'max_length': '最长是32',
        }
    )

    age = forms.IntegerField(
        min_value=28,
        max_value=55,
        label="年龄:",
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': '年龄不能为空!',
        }
    )

    email = forms.EmailField(
        max_length=32,
        label="邮箱:",
        required=True,
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={
            'required': '邮箱不能为空!',
            'invalid': '邮箱格式错误!',
        }
    )

    address = forms.CharField(
        max_length=64,
        label="地址:",
        required=True,
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={
            'required': '地址不能为空!',
            'max_length': '最长是64',
        }

    )

    