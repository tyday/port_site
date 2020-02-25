from django.contrib import admin
from .models import SensorReading

# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('name','importance','display')
#     list_editable = ('importance','display')
#     pass

admin.site.register(SensorReading)

# Register your models here.
