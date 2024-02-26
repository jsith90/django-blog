from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=False)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
