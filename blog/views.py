from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from .models import Blog, BlogType


def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 每十个分一页
    page_num = request.GET.get('page', 1)  # 获取页码参数(GET请求)
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # render_to_response()第二个参数是字典，所以先创建一个字典
    context = {}
    # 将blogs作为字典的键，所有博客作为值写入字典
    context['blogs'] = page_of_blogs.object_list
    context['blog_types'] = BlogType.objects.all()
    context['page_of_blogs'] = page_of_blogs
    context['blog_dates'] = Blog.objects.dates('create_time', 'month', order='DESC')
    context['page_range'] = page_range
    return context


def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    # 返回到博客列表中的使用
    return render_to_response('blog_list.html', context)


def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    # 用过滤器找到（类别为函数参数中的blog_type）的blog，写入字典
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render_to_response('blogs_with_type.html', context)


def blogs_with_date(request, year, month):
    # 用过滤器找到（类别为函数参数中的blog_type）的blog，写入字典
    blogs_all_list = Blog.objects.filter(create_time__year=year, create_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' % (year, month)
    return render_to_response('blogs_with_date.html', context)


def blog_detail(request, blog_pk):
    context = {}
    # 用主键寻找指定的blog导入字典，如果没找到返回404
    blog = get_object_or_404(Blog, pk=blog_pk)
    context['previous_blog'] = Blog.objects.filter(create_time__gt=blog.create_time).last()
    context['next_blog'] = Blog.objects.filter(create_time__lt=blog.create_time).first()
    context['blog'] = blog
    return render_to_response('blog_detail.html', context)