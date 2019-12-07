from django.contrib import admin

from .models import Observation,Cloud_coverage_choices, Precipitation_choices, Phenomena_choice, Profile
# Register your models here.

admin.site.register(Observation)
admin.site.register(Cloud_coverage_choices)
admin.site.register(Precipitation_choices)
admin.site.register(Phenomena_choice)
admin.site.register(Profile)
