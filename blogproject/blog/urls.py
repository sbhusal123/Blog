from django.urls import path
from . import views

urlpatterns = [
    path("list/",views.blog_post_list),
    path("new/",views.blog_post_create),
    path("post/<str:slug>/",views.blog_post_read),
    path("post/<str:slug>/edit/",views.blog_post_update),
    path("post/<str:slug>/delete/",views.blog_post_delete),
]