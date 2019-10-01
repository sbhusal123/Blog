from django.shortcuts import render
from .models import SearchQuery
from blog.models import BlogPosts


# Create your views here.

def search_view(request):
    query = request.GET["q"] or None # if doesn't exists set to None
    user = None

    if request.user.is_authenticated:
        user = request.user

    context = {}
    if query is not None:
        # SearchQuery.objects.create(user=user,query=query)
        search_item = BlogPosts.objects.search(query=query) # returns the list of objects
        context = {'blog_list':search_item,'query':query}
        print(search_item[0].title)
    return render(request,'searches/views.html',context)
