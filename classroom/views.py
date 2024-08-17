from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def home_view(request):
#    return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = "classroom/home.html"

class ThankuView(TemplateView):
    template_name = "classroom/thanku.html" 