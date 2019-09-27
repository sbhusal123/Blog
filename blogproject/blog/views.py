from django.shortcuts import render,get_object_or_404
from .models import BlogPosts
from django.http import Http404
from .forms import BlogPostForm,BlogPostModelForm

# Create your views here.



def blog_post_list(request):
    # Filtering Approaches: Documentation: https://docs.djangoproject.com/en/2.2/ref/models/querysets/
    # BlogPosts.objects.filter(title__icontains='hello')
    # BlogPosts.objects.filter(title__startswith='hello')
    obj = BlogPosts.objects.all() #try catch

    template_name = "blog_post_list.html"
    context = {"objects": obj}
    return render(request, template_name, context)

# CRUD for blog post- > Create, Read, Update, Delete

def blog_post_create(request):

    """
    Actually there are two strategies.
    i.e Extending ModelForm and SimpleForm
    """

    #Using Simple Form class
    # form = BlogPostForm(request.POST or None)
    # if form.is_valid():
        # print(form.cleaned_data)
    # BlogPosts.objects.create(**form.cleaned_data) # key-word arguments(kwargs): https://stackoverflow.com/questions/1419046/normal-arguments-vs-keyword-arguments
    # form = BlogPostForm()

    # Using Model Form
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()

    template_name = "blog_post_create.html"
    context = {'form':form}
    return render(request, template_name, context)




def blog_post_read(request,slug):
    try:
        obj = BlogPosts.objects.get(slug= slug)

    except BlogPosts.DoesNotExist:
        # Django Exception Documentation: https://docs.djangoproject.com/en/2.2/ref/exceptions/
        raise Http404



    # another way of handelling does-not-exists exception
    # obj = get_object_or_404(BlogPosts,slug=slug)

    template_name ="blog_post_read.html"
    context = {"object":obj}
    return render(request,template_name,context)





def blog_post_update(request):
    obj = []
    template_name = "blog_post_update.html"
    context = {"object": obj}
    return render(request, template_name, context)





def blog_post_delete(request):
    obj = []
    template_name = "blog_post_delete.html"
    context = {"object": obj}
    return render(request, template_name, context)
