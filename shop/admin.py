from django.contrib import admin
from .models import *


# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, catadmin)


class proadmin(admin.ModelAdmin):
    list_display = ['name','slug','img','price','stock']
    list_editable = ['img','price','stock']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products, proadmin)
