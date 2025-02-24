from django.shortcuts import render, get_object_or_404
from .models import Phone

def body(request):
    return render(request, 'home/asosiy.html')

def home(request):
    phones = Phone.objects.all()[:3]
    context = {'phones': phones}
    return render(request, 'home/home.html', context)

def products(request):
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, 'home/products.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def phone_list(request):
    phone = Phone.objects.all()
    context = {'phone': phone}
    return render(request, 'home/phone_list.html', context)

def phone_detail(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    context = {'phone': phone}
    return render(request, 'home/phone_detail.html', context)
