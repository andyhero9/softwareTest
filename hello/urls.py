"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import triangle,index,nextDay,upload

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index.index),
    url(r'^triangle/', triangle.triangle),
    url(r'^triangle-post/', triangle.triangle_post),
    url(r'^next/', nextDay.nextDay_Get),
    url(r'^next-post/', nextDay.nextDay_Post),
    url(r'^nextCsv-post/', nextDay.nextDay_Post_Csv),
    url(r'^uploadFile/', upload.loadCsv_Post),
    url(r'^traingleCsv_Post/', upload.traingleCsv_Post),
]