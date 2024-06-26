from django.contrib import admin
from .models import *
# Register your models here.


class CustomAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','role','is_staff') 

admin.site.register(CustomUser,CustomAdmin)