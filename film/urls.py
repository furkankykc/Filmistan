# coding=utf-8
"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))




To Do List:
    1. mysql kur onları yap
    2. Anasayfa tek olucak login register tek sayfa
    3.site görselleştirmeleri animasyonlar
    4. her üyeye ayrı feachured sayfası


"""


from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url
from filmistan.views import FilmList

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('filmistan.urls')),
   ]


