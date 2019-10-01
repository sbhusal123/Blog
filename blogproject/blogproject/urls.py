"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from searches.views import search_view
from . import views

urlpatterns = [
    path('',views.landing_page),
    path('home',views.home_page),
    path('blog',include('blog.urls')),
    path('contact/',views.contact),

    path('admin/', admin.site.urls),
    path('search/',include('searches.urls'))
]


# https://docs.djangoproject.com/en/2.2/howto/static-files/#managing-static-files-e-g-images-javascript-css
if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
