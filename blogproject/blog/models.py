from django.db import models
from django.utils.text import slugify
from django.conf import settings
from .managers import BlogPostsQuerySet,BlogPostsManager

# get the user model from django admin
User = settings.AUTH_USER_MODEL
"""
while in views :
from djangp.contrib.auth import get_user_model
User = get_user_model()
"""

# Create your models here.
class BlogPosts(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.SET_NULL,null=True)
    """
        default =1 is used to provide default value for user in this model from first entry in the User Table
        on_delete = models.SET_NULL sets the user=NULL when corrosponding ForeignKey user is deleted    
    """

    image = models.FileField(upload_to='images/',blank=True,null=True)
    title = models.CharField(max_length=50,unique=True,blank=False)
    slug = models.SlugField() # basicaly used in lookup through URL.
    content = models.TextField(null=True,blank=True)


    published_date = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True) # time when created
    updated = models.DateTimeField(auto_now=True) # time when saved,modified

    """
        A DateTimeField has two optional parameters:
        -> auto_now_add sets the value of the field to current datetime when the object is created.
        -> auto_now sets the value of the field to current datetime every time the field is saved.
        -> These options and the default parameter are mutually exclusive.
        
        Note: Check those from admin_panel by editing blog post.
        
    """

    objects = BlogPostsManager() # instance of the model manager

    class Meta:
        """
            For most recent post : "-published_date"
            For oldest post : "published_date"
        """
        ordering =['-published_date','-updated','-timestamp']
        # ORDER BY `blog_blogposts`.`published_date` DESC, `blog_blogposts`.`updated` DESC, `blog_blogposts`.`timestamp` DESC


    #overriding model method: https://docs.djangoproject.com/en/2.2/topics/db/models/#overriding-predefined-model-methods
    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super(BlogPosts,self).save(*args,**kwargs)
        return

    def __str__(self):
        return self.title

    # defining cusotom url links. Can be accessed on template using {{<object_name>.get_read_url,...}}
    def get_read_url(self):
        return f'/blog/{self.slug}'

    def get_edit_url(self):
        return f'{self.get_read_url()}/edit'

    def get_delete_url(self):
        return f'{self.get_read_url()}/delete'