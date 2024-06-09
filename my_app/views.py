from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

articles = {
    'sports' : 'Sports Page',
    'finance' : 'Finance Page',
    'politics' : 'PoIitics Page'
}

# def index(request):
#     return HttpResponse("Hello This is a View Inside My_App")

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = "Topic Not Found"
        #return HttpResponseNotFound(result)
        raise Http404("404 Generic Error") # 추후 404.html에 연결

def add_view(request, num1, num2):
    # domain.com/my_app/num1/num2 --> num1+num2
    result = num1 + num2
    return HttpResponse(str(result))