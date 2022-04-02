from django.contrib import admin
from .models import Pages

class PagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    search_fields = ('title', 'content')

# Register your models here.
admin.site.register(Pages, PagesAdmin)