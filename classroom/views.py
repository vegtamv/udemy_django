from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactForm

# Create your views here.
# def home_view(request):
#    return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = "classroom/home.html"

class ThankuView(TemplateView):
    template_name = "classroom/thanku.html" 

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html" 

    # Success URL (Not HTML file)
    # success_url = "/classroom/thanku/" 
    success_url = reverse_lazy('classroom:thanku')

    # What to do with form
    def form_valid(self, form):
        #form.save()
        print(form.cleaned_data)
        return super().form_valid(form)