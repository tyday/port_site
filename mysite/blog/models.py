import os
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver

from common.utilities.image_manipulation import rotate_image, create_responsive_images

# Create your models here.

class WebLink(models.Model):
    name = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=100)
    image_file = models.ImageField(null=True,blank=True)
    alt_text = models.CharField(max_length=100)
    source_set = models.TextField(blank=True, null=True)

    # I'm not decided on this so I'm going to keep it in for now in comment form. I may need it later.
    # generic relation stuff
    # https://simpleisbetterthancomplex.com/tutorial/2016/10/13/how-to-use-generic-relations.html
    # https://docs.djangoproject.com/en/2.1/ref/contrib/contenttypes/#generic-relations
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey()

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # photo = models.ImageField(null=True,blank=True)
    # photo_alt_text = models.CharField(max_length=200, blank=True,null=True)

    # photo = models.ManyToManyField(Image)
    photo  = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
    def publish(self):
        self.puplished_date = timezone.now()
        self.save()
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title

    
class Project(models.Model):
    name = models.CharField(max_length=200)
    # the short description is for the front page. I'm debating whether to use a CharField with a max_length rather than a TextField
    short_description = models.TextField()
    description = models.TextField()
    images = models.ManyToManyField(Image)
    githublink = models.CharField(max_length=200, blank=True, null=True)
    post = models.ManyToManyField(Post, blank=True)
    weblink = models.ManyToManyField(WebLink, blank=True)

    # Importance is rank to determine order. Higher importance items go first
    # display is a boolean to determine whether to display or not
    importance = models.IntegerField()
    display = models.BooleanField()
    date_added = models.DateTimeField(default=timezone.now)
    date_last_modified = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        self.date_last_modified = timezone.now()
        # self.save()
        super().save(*args, **kwargs)  # Call the "real" save() method.
    
    def __str__(self):
        return self.name

@receiver(post_save, sender=Image, dispatch_uid="update_image")
def update_image(sender, instance, **kwargs):
    if instance.image_file:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fullpath = BASE_DIR + instance.image_file.url
        rotate_image(fullpath)

        # Creates responsive images
        # then return a string consisting of the srcset
        srcset = create_responsive_images(fullpath, instance.image_file.url)
        instance.source_set = srcset

        post_save.disconnect(update_image, sender=Image, dispatch_uid="update_image")
        instance.save()
        post_save.connect(update_image, sender=Image, dispatch_uid="update_image")