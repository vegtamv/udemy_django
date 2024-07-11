from django.http import HttpResponse
from django.shortcuts import render

def my_custom_page_not_found_view(request, exception):
    return render(request, 'error_view.html', status=404)

def home_view(request):
    a = 1
    b = 2
    return HttpResponse(f"HOME VIEW {a+b}")