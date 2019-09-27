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
    # content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = BlogPosts
        fields = ['title','content']

    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if BlogPosts.objects.filter(title=title).exists():
            # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups
            raise forms.ValidationError("This title has already been used. Please use another title")
        return title




