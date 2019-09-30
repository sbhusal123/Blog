from django.shortcuts import render,get_object_or_404, redirect
from .models import BlogPosts
from django.http import Http404
from .forms import BlogPostForm,BlogPostModelForm
# from django.utils import timezone
# from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required # staff member is a field in

# Create your views here.

"""
Caution: Use try catch exception handling strategy while fetching objects.     
"""


"""
    Filtering a published post. Two methods:
        1. Filtering on each view where blog is being retrived. (violates DRY due to code redundancy)
            from django.utils import timezone
            now = timezone.now()
            qs = BlogPosts.objects.filter(published_date__gte=now)
                        
        2. Using Custom Model Manager on model class.
           -> Defined in the model class.
"""

def blog_post_list(request):
    # Filtering Approaches: Documentation: https://docs.djangoproject.com/en/2.2/ref/models/querysets/
    # BlogPosts.objects.filter(title__icontains='hello')
    # BlogPosts.objects.filter(title__startswith='hello')

    """
    Filtering weather the blog is published or not. Violates DRY. NOt to use this.
        now = timezone.now()
        obj = BlogPosts.objects.filter(published_date__gte=now) #try catch
    """


    qs = BlogPosts.objects.all().published()

    if request.user.is_authenticated:
        my_qs = BlogPosts.objects.filter(user=request.user)
        qs = (qs| my_qs).distinct()
    # print("\n\n")
    # print(qs.query)
    # print("\n\n")
    template_name = "blog_post_list.html"
    context = {"objects": qs}
    return render(request, template_name, context)

# CRUD for blog post- > Create, Read, Update, Delete


"""
@login_required: Description

Definition:
    1. @login_required # by default admin login is required. Basically checks the session
       -> Can also be defined in settings.py file as: LOGIN_URL =".../". 
       -> When defined in settings.py no need to pass it explicitly as LOGIN_URL will be grabbed from settings.py file.
         
    2. @login_required(login_url=".../") #checks weather the user has loged in the url '.../'
    
@staff_member_required: Description
    Checks weather the logged in admin user is staff or not.
    Staff is a bloean field in User table.  
"""
# @login_required(login_url="login/") #login url can be passed explicitly
@staff_member_required # staff is a boolean field value in django admin User's database
def blog_post_create(request):

    """
    Can be achieved using form. Actually there are two strategies.
         1. Extending ModelForm (better strategy)
         2.  SimpleForm
    """

    #Using Simple Form class
    # form = BlogPostForm(request.POST or None)
    # if form.is_valid():
        # print(form.cleaned_data)
    # BlogPosts.objects.create(**form.cleaned_data) # key-word arguments(kwargs): https://stackoverflow.com/questions/1419046/normal-arguments-vs-keyword-arguments
    # form = BlogPostForm()

    """ If not using authentication decorators, can check weather a user is authenticated using request.user.is_authenticated:"""
    # if not request.user.is_authenticated: (for staff member: request.user.is_staff)
    #     return render(request,'error_template.html',context)

    # Using Model Form
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
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
        return redirect("/blog/")

    template_name = "blog_post_update.html"
    context = {"form": form}
    return render(request, template_name,context)

@staff_member_required
def blog_post_delete(request,slug):

    obj = get_object_or_404(BlogPosts,slug=slug)

    if request.method == "POST":
        obj.delete()
        return redirect("/blog/")

    template_name = "blog_post_delete.html"
    context = {"object": obj}
    return render(request, template_name, context)