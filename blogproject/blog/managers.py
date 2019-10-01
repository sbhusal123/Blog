"""
Custom querysets: https://docs.djangoproject.com/en/2.2/topics/db/managers/#calling-custom-queryset-methods-from-the-manager
Custom Models: https://docs.djangoproject.com/en/2.2/topics/db/managers/#modifying-a-manager-s-initial-queryset
"""
from django.utils import timezone
from django.db import models
from django.db.models import Q

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
        return self.filter(published_date__lte=now)  # appends  `WHERE `blog_blogposts`.`published_date` >= 2019-09-29 04:10:26.953146`

    def search(self,query):
        """
            Complex look ups: https://docs.djangoproject.com/en/2.2/topics/db/queries/#complex-lookups-with-q-objects
            | = or (pipe)
        """
        lookup = (
            Q(title__icontains = query) |
            Q(content__icontains=query)
            # | Q(user__username__icontains=query) |
        )
        return self.filter(title__icontains=query)

class BlogPostsManager(models.Manager):
    """
        -> Every model has at least one Manager.
        -> Model managers won't work in case of custom query sets. For eg: BlogPosts.objects.all().published()
        -> So in order to use in case of custom query sets, must be able to modify the custom query customs

        Note:
            Every custom QuerySets(extending QuerySets) must be called from it's custom model Manager.
    """

    def get_queryset(self):
        return BlogPostsQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self,query):
        return self.get_queryset().search(query)