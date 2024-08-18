from django.urls import path
#from .views import home_view
from .views import HomeView, ThankuView, ContactFormView,TeacherCreateView,TeacherListView, TeacherDetailView

app_name = 'classroom'

urlpatterns = [
    #path('',home_view,name='home')
    path('',HomeView.as_view(),name='home'),
    path('thanku/',ThankuView.as_view(),name='thanku'),
    path('contact/',ContactFormView.as_view(),name='contact'),
    path('create_teacher/',TeacherCreateView.as_view(),name='create_teacher'),
    path('list_teacher/',TeacherListView.as_view(),name='list_teacher'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='detail_teacher')
]