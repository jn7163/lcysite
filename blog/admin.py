from django.contrib import admin

from .models import Author,Passage,Reply
# Register your models here.
admin.site.register(Passage)
admin.site.register(Author)
admin.site.register(Reply)