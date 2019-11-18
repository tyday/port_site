import os
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver

from common.utilities.image_manipulation import rotate_image, create_responsive_images

# Create your models here.


class Cloud_coverage_choices(models.Model):
    cloud_coverage_short = models.CharField(max_length=255)
    cloud_coverage_long = models.CharField(max_length=255)

    def __str__(self):
        return self.cloud_coverage_long


class Precipitation_choices(models.Model):
    precipitation_type = models.CharField(max_length=255)

    def __str__(self):
        return self.precipitation_type


class Phenomena_choice(models.Model):
    phenomena = models.CharField(max_length=255)

    def __str__(self):
        return self.phenomena


class Observation(models.Model):
    observer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    observation_date = models.DateTimeField(default=timezone.now)
    latitude = models.DecimalField(max_digits=7, decimal_places=4, blank=True)
    longitude = models.DecimalField(max_digits=7, decimal_places=4, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)

    perceived_outdoor_temperature = models.DecimalField(
        max_digits=4, decimal_places=1)
    perceived_outdoor_humidity = models.IntegerField()
    observed_outdoor_temperature = models.DecimalField(
        max_digits=4, decimal_places=1, blank=True, null=True)
    observed_outdoor_humidity = models.IntegerField(blank=True, null=True)
    observed_pressure_millibars = models.IntegerField(blank=True, null=True)

    surface_wind_direction = models.IntegerField()
    surface_wind_speed = models.IntegerField()
    aloft_wind_direction = models.IntegerField(blank=True, null=True)
    aloft_wind_speed = models.IntegerField(blank=True, null=True)

    cloud_observation = models.CharField(max_length=255)
    cloud_coverage = models.ForeignKey(
        Cloud_coverage_choices, on_delete=models.CASCADE, blank=True, null=True)

    precipitation_observation = models.ForeignKey(
        Precipitation_choices, on_delete=models.CASCADE, blank=True, null=True)
    phenomena_observation = models.ForeignKey(
        Phenomena_choice, on_delete=models.CASCADE, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    source_set = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.observation_date)
    
    def get_absolute_url(self):
        return reverse('observation_detail', args=[str(self.id)])

    # Tried using this function to return a srcset. The problem I ran into was
    # The widths weren't accurate with pictures taller than wide.
    # Decided to handle building the srcset in the pre-save signal
    # and adding a srcset field to the db. This seems like a much better
    # idea since the srcset has accurate widths now
    # def get_srcset(self):
    #     try:
    #         if self.image:            
    #             srcset = []
    #             srcset_text = ""
    #             srcset_url = ""
    #             srcset_size = ""
    #             sizes = ['100','500','1000']

    #             file, extension = self.image.url.split('.')
    #             directory = os.path.dirname(self.image.path)
    #             basename, ext = os.path.basename(self.image.path).split('.')
    #             # fullpath = os.path.join(directory)

    #             for size in sizes:
    #                 filename = basename + '_' + size + '.' + ext
    #                 fileurl = file + '_' + size + '.' + ext

    #                 if os.path.exists(os.path.join(directory,filename)):
    #                     # srcset.append({
    #                     #     'url': fileurl,
    #                     #     'width': size
    #                     # })
    #                     srcset_text += fileurl + " " + size + "w" + ", "
    #                 else:
    #                     # print('nothing found')
    #                     pass
    #             # print(srcset)
    #             srcset_text += self.image.url + " " + str(self.image.width) + "w"
    #             return srcset_text
    #         else:
    #             return None
    #     except Exception as e:
    #         print(f'Error in get_srcset {e}')
    #         return None


@receiver(post_save, sender=Observation, dispatch_uid="update_image_observation")
def update_image(sender, instance, **kwargs):
    if instance.image:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fullpath = BASE_DIR + instance.image.url
        rotate_image(fullpath)

        # Creates responsive images
        # then return a string consisting of the srcset
        srcset = create_responsive_images(fullpath, instance.image.url)
        instance.source_set = srcset

        post_save.disconnect(update_image, sender=Observation, dispatch_uid="update_image_observation")
        instance.save()
        post_save.connect(update_image, sender=Observation, dispatch_uid="update_image_observation")
