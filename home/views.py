from django.shortcuts import render, get_object_or_404, redirect
from .models import Phone, Comment

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

def phone_detail(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    comments = Comment.objects.filter(phone=phone).order_by('-created_date')
    context = {'phone': phone, 'comments': comments}
    return render(request, 'home/phone_detail.html', context)

def phone_create(request):
    phone = Phone()
    if request.method == 'POST':
        phone.brand = request.POST.get('brand', '')
        phone.model = request.POST.get('model', '')
        phone.color = request.POST.get('color', '')
        phone.price = request.POST.get('price', 0)
        phone.description = request.POST.get('description', '')
        phone.image = request.FILES.get('image')
        phone.save()
        return redirect('products')
    return render(request, 'home/phone_create.html', {'phone': phone})


def phone_update(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    if request.method == 'POST':
        phone.brand = request.POST.get('brand', phone.brand)
        phone.model = request.POST.get('model', phone.model)
        phone.color = request.POST.get('color', phone.color)
        phone.price = request.POST.get('price', phone.price)
        phone.description = request.POST.get('description', phone.description)
        phone.image = request.FILES.get('image', phone.image)
        phone.save()
        return redirect('phone_detail', pk=phone.pk)
    return render(request, 'home/phone_update.html', {'phone': phone})


def phone_delete(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('products')
    return render(request, 'home/phone_delete.html', {'phone':phone})

def add_comment(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        if name and text:
            Comment.objects.create(phone=phone, name=name, text=text)
            return redirect('phone_detail', pk=phone.pk)
    return render(request, 'home/add_comment.html', {'phone': phone})



