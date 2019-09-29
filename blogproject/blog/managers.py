"""
Custom querysets: https://docs.djangoproject.com/en/2.2/topics/db/managers/#calling-custom-queryset-methods-from-the-manager
Custom Models: https://docs.djangoproject.com/en/2.2/topics/db/managers/#modifying-a-manager-s-initial-queryset
"""
from django.utils import timezone
from django.db import models

class BlogPostsQuerySet(models.QuerySet):
    def published(self):
        """
          Actually what this does is modifies the query set to filter with certain conditions
        """
        now = timezone.now()

        """
            self.get_queryset() = query trying to be fetched from the view
              ex. self.get_queryset() = BlogPosts.objects.all()  

            Note: Make a instance of this (Manager class) in the Model class. 
        """
        return self.filter(
            published_date__gte=now)  # appends  `WHERE `blog_blogposts`.`published_date` >= 2019-09-29 04:10:26.953146`


class BlogPostsManager(models.Manager):
    """
        -> Every model has at least one Manager.
        -> Model managers won't work in case of custom query sets. For eg: BlogPosts.objects.all().published()
        -> So in order to use in case of custom query sets, must be able to modify the custom query customs
    """

    def get_queryset(self):
        return BlogPostsQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()