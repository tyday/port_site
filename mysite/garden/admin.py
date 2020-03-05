from django.contrib import admin
from .models import ProjectConnection, SensorReading

# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('name','importance','display')
#     list_editable = ('importance','display')
#     pass
class SensorReadingAdmin(admin.ModelAdmin):
    list_display = ('id','sensorID', 'temp1', 'temp2', 'rh1', 'rh2','light','timestamp')

admin.site.register(SensorReading, SensorReadingAdmin)
admin.site.register(ProjectConnection)

# Register your models here.
