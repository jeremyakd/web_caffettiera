from django.contrib.admin import register, ModelAdmin
from .models import Page

@register(Page)
class PageAdmin(ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','ordering')
