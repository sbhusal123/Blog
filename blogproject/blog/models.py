from django.db import models
from django.utils.text import slugify

# Create your models here.

class BlogPosts(models.Model):
    title = models.CharField(max_length=50,unique=True,blank=False)
    slug = models.SlugField() # basicaly used in lookup through URL.
    content = models.TextField(null=True,blank=True)

    #method called when saving objects using ORM
    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super(BlogPosts,self).save(*args,**kwargs)
        return

    def __str__(self):
        return self.title