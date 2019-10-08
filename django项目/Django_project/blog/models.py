from django.db import models

# Create your models here.


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    avatar = models.FileField(upload_to="./avatar",default="default.jpg",null=True,blank=True)
    create_time = models.DateTimeField(auto_now=True)

    blog = models.OneToOneField(
        to="Blog",
        to_field="nid",
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

#Blog系统相关表
class Blog(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    site = models.CharField(max_length=32,unique=True)
    theme = models.CharField(max_length=32)

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = "Blog站点"
        verbose_name_plural = verbose_name


class Category(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    blog = models.ForeignKey(to="Blog",to_field="nid",on_delete=models.CASCADE) #外键关联博客，一个博客站点可以有多个分类

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name

class Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)#标签名、
    blog = models.ForeignKey(to="Blog",to_field="nid",on_delete=models.CASCADE) #所属博客


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

class Article(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    comment_count = models.IntegerField(verbose_name="评论数",default=0)
    up_count = models.IntegerField(verbose_name="点赞数",default=0)
    down_count = models.IntegerField(verbose_name="踩数",default=0)
    category = models.ForeignKey(to="Category",to_field="nid",null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(to="UserInfo",to_field="id",on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        to="Tag",
        through = "Article2Tag",
        through_fields = ("article","tag"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name



class ArticleDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    content = models.TextField()
    article = models.OneToOneField(to="Article",to_field="nid",on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "文章详情"
        verbose_name_plural = verbose_name

class Article2Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article",to_field="nid",on_delete=models.CASCADE)
    tag = models.ForeignKey(to="Tag",to_field="nid",on_delete=models.CASCADE)

    class Meta:
        unique_together = (("article","tag"),)
        verbose_name = "文章-标签"
        verbose_name_plural = verbose_name


class ArticleUpDown(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to="UserInfo",null=True,on_delete=models.CASCADE)
    article = models.ForeignKey(to="Article",null=True,on_delete=models.CASCADE)
    is_up = models.BooleanField(default=True)

    class Meta:
        unique_together = (("article","user"),)
        verbose_name = "文章点赞"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid",on_delete=models.CASCADE)
    user = models.ForeignKey(to="UserInfo", to_field="id",on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return  self.content



    class Meta:
        verbose_name = "用户评论"
        verbose_name_plural = verbose_name


#学校管理系统
class Classes(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Student(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField(max_length=32)
    email = models.EmailField(max_length=64)
    address = models.CharField(max_length=128)
    cls = models.ForeignKey(to="Classes",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.EmailField(max_length=64)
    address = models.CharField(max_length=128)
    c2t = models.ManyToManyField(to="Classes")

    def __str__(self):
        return self.name


