from django.contrib import admin
from tracker.models import *



class CarCountAdmin(admin.ModelAdmin):
    list_display = ['time', 'count']


# Register your models here.
admin.site.register(Car_Count, CarCountAdmin)