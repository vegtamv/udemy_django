from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ContactForm
from .models import Teacher

# Create your views here.
# def home_view(request):
#    return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = "classroom/home.html"

class ThankuView(TemplateView):
    template_name = "classroom/thanku.html" 

class TeacherCreateView(CreateView):
    # Template = [model]_form.html
    # Model에 연결
    model = Teacher 
    # 표시하려는 속성
    fields = '__all__'
    # 성공 후 이동되는 URL
    success_url = reverse_lazy('classroom:thanku')

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
    
class TeacherListView(ListView):
    # Template = [model]_list.html
    # Model에 연결
    model = Teacher 
    context_object_name = "teacher_list" # default = object_list


class TeacherDetailView(DetailView):
    # Template = [model]_detail.html
    # Model에 연결
    model = Teacher 


class TeacherUpdateView(UpdateView):
    # Template = [model]_form.html
    # Model에 연결
    model = Teacher 
    fields = ['subject']

    # 성공 후 이동되는 URL
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
    # Template = [model]_confirm_delete.html
    # Model에 연결
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')
