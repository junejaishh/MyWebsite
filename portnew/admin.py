from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Users)
admin.site.register(filestorage)
admin.site.register(Post)
admin.site.register(Picture)
admin.site.register(About)
admin.site.register(Project)