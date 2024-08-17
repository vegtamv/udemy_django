from django.urls import path
#from .views import home_view
from .views import HomeView, ThankuView, ContactFormView

app_name = 'classroom'

urlpatterns = [
    #path('',home_view,name='home')
    path('',HomeView.as_view(),name='home'),
    path('thanku/',ThankuView.as_view(),name='thanku'),
    path('contact/',ContactFormView.as_view(),name='contact')
]