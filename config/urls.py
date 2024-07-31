"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include # app의 urls.py 연결 위해 import
from django.http.response import HttpResponse
from . import views # 프로젝트 레벨의 Views.py import

def home_view (request):
    return HttpResponse("HOME PAGE")

urlpatterns = [
    #path('', home_view, name='home'), # 프로젝트 레벨의 urls.py의 home_view 연결
    path('', views.home_view, name='home'), # 프로젝트 레벨의 views.py의 home_view 연결
    path('my_app/', include('my_app.urls')), # my_app의 urls.py 연결
    path('cars/', include('cars.urls')), # cars의 urls.py 연결
    path('admin/', admin.site.urls),
]

handler404 = 'config.views.my_custom_page_not_found_view'