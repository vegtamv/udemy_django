from django.urls import path
from . import views

# app namespace 등록
app_name = "my_app"

urlpatterns = [
    path('', views.simple_view, name='example'), # domain.com/my_app
    path('variable', views.variable_view, name='variable')
]

# urlpatterns = [
    #path('', views.index, name="index"), #/my_apps --> Project urls.py,
    # path('<int:num_page>', views.num_page_view), # /my_apps/num_page
    # path('<str:topic>', views.news_view, name="topic-page"), # /my_apps/topic   
    #path('<int:num1>/<int:num2>', views.add_view) # /my_apps/topic
# ]