from django.contrib import admin

# Register your models here.
from home.models import Blogpost


class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('post','date')
admin.site.register(Blogpost)