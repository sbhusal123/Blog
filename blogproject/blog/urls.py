from django.urls import path
from . import views

urlpatterns = [
    path("/details/<int:post_id >/$",views.blog_post_detail_page)
]