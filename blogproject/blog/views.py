from django.shortcuts import render,get_object_or_404, redirect
from .models import BlogPosts
from django.http import Http404
from .forms import BlogPostForm,BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required # staff member is a field in

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


"""
@login_required: Description

Definition:
    1. @login_required # by default admin login is required. Basically checks the session
       -> Can also be defined in settings.py file as: LOGIN_URL =".../". When defined no need to pass it explicitly 
       -> as LOGIN_URL will be grabbed from settings.py file.
         
    2. @login_required(login_url=".../) #checks weather the user has loged in the '.../'
    
@staff_member_required: Description
    Checks weather the logged in admin user is staff or not.
    Staff is a bloean field in User table.  
"""


@login_required(login_url="login/") #login url can be passed explicitly
@staff_member_required # staff is a boolean field value in django admin User's database
def blog_post_create(request):

    """
    Actually there are two strategies.
    i.e Extending ModelForm or SimpleForm
    """

    #Using Simple Form class
    # form = BlogPostForm(request.POST or None)
    # if form.is_valid():
        # print(form.cleaned_data)
    # BlogPosts.objects.create(**form.cleaned_data) # key-word arguments(kwargs): https://stackoverflow.com/questions/1419046/normal-arguments-vs-keyword-arguments
    # form = BlogPostForm()

    """ If not using authentication decorators, can check weather a user is authenticated using request.user.is_authenticated:"""
    # if not request.user.is_authenticated:
    #     return render(request,'error_template.html',context)

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

@staff_member_required
def blog_post_update(request,slug):

    obj = get_object_or_404(BlogPosts,slug=slug)
    form = BlogPostModelForm(request.POST or None,instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/blog/list")

    template_name = "blog_post_update.html"
    context = {"form": form}
    return render(request, template_name,context)


def blog_post_delete(request):
    obj = []
    template_name = "blog_post_delete.html"
    context = {"object": obj}
    return render(request, template_name, context)