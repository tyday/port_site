from django.contrib import admin
from .models import Post, Project, Image, WebLink

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','importance','display')
    list_editable = ('importance','display')
    pass

admin.site.register(Post)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image)
admin.site.register(WebLink)