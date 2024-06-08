from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name="index"), #/my_apps --> Project urls.py,
    path('<topic>', views.news_view), # /my_apps/topic
    path('<int:num1>/<int:num2>', views.add_view) # /my_apps/topic
]