from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name="index"), #/my_apps --> Project urls.py,
    path('<int:num_page>', views.num_page_view), # /my_apps/num_page
    path('<str:topic>', views.news_view, name="topic-page"), # /my_apps/topic   
    #path('<int:num1>/<int:num2>', views.add_view) # /my_apps/topic
]