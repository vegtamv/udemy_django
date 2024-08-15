from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from .forms import ReviewForm

# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars':all_cars}

    return render(request, 'cars/list.html', context=context)

def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        # 유저가 새 Car를 등록했다면 list.html로 이동
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def delete(request):
        if request.POST:
            pk = request.POST['pk'] 
            try:
                models.Car.objects.get(pk=pk).delete()
                return redirect(reverse('cars:list'))
            except:
                print('pk not found')
                return redirect(reverse('cars:list'))
        else:
            return render(request, 'cars/delete.html')
        
def rental_review(request):

    # POST Request -> FORM Contents -> Thank you page
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('cars:thank_you'))
        
    # Else, Render Form
    else:
        form = ReviewForm()
        return render(request, 'cars/rental_review.html', context={'form':form})

def thank_you(request):
    return render(request, 'cars/thank_you.html')