from django import forms
from .models import BlogPosts

class BlogPostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

"""
Request response with form:
Request -> URL -> Views -> Form -> Model -> Response 
"""

class BlogPostModelForm(forms.ModelForm):
    """
    Even the fields can be modifled as below
    """
    title = forms.CharField()
    published_date = forms.DateTimeField(widget=forms.SelectDateWidget)
    # content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = BlogPosts
        fields = ['title','content','published_date','image']

    def clean_title(self,*args,**kwargs):
        instance = self.instance
        print(instance)
        title = self.cleaned_data.get("title")
        qs = BlogPosts.objects.filter(title__iexact=title) ## https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups

        """
        Why two conditional statements?
        -> Because the same form in being used for updating and for new blog post.
        
        -> Basically when new blog post is created, instance is empty,
           while for updating instance, there is some instance as we have passed from views to the form.                   
        """
        if instance is not None: # when updating blog content
           qs = qs.exclude(pk = instance.pk) # prevent validation on instance itself


        if qs.exists(): # when creating new blog if, blog with the newly passed title exists
            raise forms.ValidationError("This title has already been used. Please use another title")

        return title