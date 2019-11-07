from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class BlogType(models.Model):
    # 博客类型模型
    type_name = models.CharField(max_length=15)

    def __str__(self):
        # 用来定义显示出来的文本
        return self.type_name


# Create your models here.
class Blog(models.Model):
    # 创建博客模型
    title = models.CharField(max_length=50)     # 标题
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)        # 博客类型，从BlogType类导入
    content = RichTextUploadingField()        # 内容
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)       # 作者,从User类下导入
    create_time = models.DateTimeField(auto_now_add=True)       # 创建时间
    last_updated_time = models.DateTimeField(auto_now=True)     # 最后修改时间

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-create_time']