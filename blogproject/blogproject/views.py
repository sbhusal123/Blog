from django.shortcuts import render
from .forms import ContactForm
from django.apps import apps
from blog.models import BlogPosts

# BlogPosts = apps.get_model('blog', 'BlogPosts')


def home_page(request):
    qs = BlogPosts.objects.all()[:5]
    context = {
        'blog_list' :qs
    }
    return render(request,'home.html',context)

def landing_page(request):
    return render(request,'landing_page.html')

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # form.cleaned_data # preventing from XSS, sql_injection, ...
        print(form.cleaned_data["email"])
        form = ContactForm()
    return render(request,'contact.html',{'form':form})
