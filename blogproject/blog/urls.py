from django.urls import path
from . import views

urlpatterns = [
    path("/",views.blog_post_list),
    path("-new/",views.blog_post_create),
    path("/<str:slug>/",views.blog_post_read),
    path("/<str:slug>/edit/",views.blog_post_update),
    path("/<str:slug>/delete/",views.blog_post_delete),
]