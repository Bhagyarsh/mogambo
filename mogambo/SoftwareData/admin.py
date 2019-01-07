from django.contrib import admin
from .models import Software, Category, ScreenShot, Comment,  Tag
# Register your models here.

admin.site.register(Software)
admin.site.register(Category)
admin.site.register(ScreenShot)
admin.site.register(Comment)
admin.site.register(Tag)
