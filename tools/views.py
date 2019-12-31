from django.shortcuts import render
from .models import Tool


def tools_list(request):
    tools_all_list = Tool.objects.all()
    context = {}
    context['tools'] = tools_all_list
    return render(request, 'tools.html', context)
