from django.db import models
from django.utils.text import slugify
from django.conf import settings

User = settings.AUTH_USER_MODEL # to use in model(as foreign key field) import from django.conf
"""
while in views :

from djangp.contrib.auth import get_user_model

User = get_user_model()
"""


# Create your models here.

class BlogPosts(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.SET_NULL,null=True)
    # default =1 is used to provide default value for user in this model from first entry in the User Table
    # on_delete

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

    def get_read_url(self):
        return f'/blog/{self.slug}'

    def get_edit_url(self):
        return f'{self.get_read_url()}/edit'

    def get_delete_url(self):
        return f'{self.get_read_url()}/delete'
