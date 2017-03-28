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
from hello import triangle, index, nextDay, views, sales
import hello

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^index/', index.index),
	# url(r'^index.html/', index.index),
	url(r'^triangle/', triangle.triangle_post),
	# url(r'^calendar.html/', calendar.calendar),
	# url(r'^triangle-post/', triangle.triangle_post),
	url(r'^next/', nextDay.nextDay_Get),
	url(r'^next-post/', nextDay.nextDay_Post),
	url(r'^nextCsv-post/', nextDay.nextDay_Post_Csv),
	url(r'^triangle_input/', triangle.triangle_input),
	url(r'^sale_input/', sales.sales_Post),
	url(r'^sales/', sales.csv_sales_Post),
	url(r'^toIndex/$', hello.views.toIndex, name='toIndex'),
	url(r'^toNextday/$', hello.views.toNextDay, name='toNextDay'),
	url(r'^toCommission/$', hello.views.toCommission, name='toCommission')
]
