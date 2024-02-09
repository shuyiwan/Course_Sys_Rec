"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from search import views as search_views
from shoppingCart import views as sc_views
#import search
#import shoppingCart

urlpatterns = [
    path("admin/", admin.site.urls),
    path("search/", search_views.search_keywords, name="search_keywords"), # add url path for search feature
    path("shoppingCart/", sc_views.add_classes, name="add_classes") # add url path for adding classes to cart
]
