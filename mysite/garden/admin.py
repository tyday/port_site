from django.contrib import admin
from .models import ProjectConnection, SensorReading

# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('name','importance','display')
#     list_editable = ('importance','display')
#     pass

admin.site.register(SensorReading)
admin.site.register(ProjectConnection)

# Register your models here.
