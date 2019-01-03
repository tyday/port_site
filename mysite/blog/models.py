from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(null=True,blank=True)
    photo_alt_text = models.CharField(max_length=200, blank=True,null=True)

    def publish(self):
        self.puplished_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Image(models.Model):
    name = models.CharField(max_length=100)
    image_file = models.ImageField(null=True,blank=True)
    alt_text = models.CharField(max_length=100)

    # I'm not decided on this so I'm going to keep it in for now in comment form. I may need it later.
    # generic relation stuff
    # https://simpleisbetterthancomplex.com/tutorial/2016/10/13/how-to-use-generic-relations.html
    # https://docs.djangoproject.com/en/2.1/ref/contrib/contenttypes/#generic-relations
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey()

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=200)
    # the short description is for the front page. I'm debating whether to use a CharField with a max_length rather than a TextField
    short_description = models.TextField()
    description = models.TextField()
    images = models.ManyToManyField(Image)

    # Importance is rank to determine order. Higher importance items go first
    # display is a boolean to determine whether to display or not
    importance = models.IntegerField()
    display = models.BooleanField()
    date_added = models.DateTimeField(default=timezone.now)
    date_last_modified = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name