from django.contrib import admin

# Register your models here.
from .models import Linux, OsVersion, Error, PackageManager,Command


admin.site.register(Linux)
admin.site.register(OsVersion)
admin.site.register(Error)
admin.site.register(PackageManager)
admin.site.register(Command)
