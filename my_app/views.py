from django.shortcuts import render
from django.http import HttpResponse

articles = {
    'sports' : 'Sports Page',
    'finance' : 'Finance Page',
    'politics' : 'PoIitics Page'
}

# def index(request):
#     return HttpResponse("Hello This is a View Inside My_App")

def news_view(request, topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2):
    # domain.com/my_app/num1/num2 --> num1+num2
    result = num1 + num2
    return HttpResponse(str(result))