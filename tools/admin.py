from django.contrib import admin
from .models import Tool


@admin.register(Tool)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')