from django.shortcuts import render_to_response,get_object_or_404
from.models import Blog, BlogType


def blog_list(request):
    # render_to_response()第二个参数是字典，所以先创建一个字典
    context = {}
    # 将blogs作为字典的键，所有博客作为值写入字典
    context['blogs'] = Blog.objects.all()
    context['blog_types'] = BlogType.objects.all()
    # 返回到博客列表中的使用
    return render_to_response('blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {}
    # 用主键寻找指定的blog导入字典，如果没找到返回404
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog_detail.html', context)


def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blog_type'] = blog_type
    # 用过滤器找到（类别为函数参数中的blog_type）的blog，写入字典
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blogs_with_type.html', context)