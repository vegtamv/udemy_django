from django.urls import path
#from .views import home_view
from .views import HomeView, ThankuView, ContactFormView,TeacherCreateView,TeacherListView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView

app_name = 'classroom'

urlpatterns = [
    #path('',home_view,name='home')
    path('',HomeView.as_view(),name='home'),
    path('thanku/',ThankuView.as_view(),name='thanku'),
    path('contact/',ContactFormView.as_view(),name='contact'),
    path('create_teacher/',TeacherCreateView.as_view(),name='create_teacher'),
    path('list_teacher/',TeacherListView.as_view(),name='list_teacher'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='detail_teacher'),
    path('update_teacher/<int:pk>', TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>', TeacherDeleteView.as_view(), name='delete_teacher')
]