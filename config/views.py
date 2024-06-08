from django.http import HttpResponse

def home_view(request):
    a = 1
    b = 2
    return HttpResponse(f"HOME VIEW {a+b}")