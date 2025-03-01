from django.shortcuts import render, get_object_or_404, redirect
from .forms import PhoneForm, CommentForm
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
    form = PhoneForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, 'home/phone_create.html', {'form': form})


def phone_update(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phone_detail', pk=phone.pk)
    else:
        form = PhoneForm(instance=phone)
    return render(request, 'home/phone_update.html', {'form': form, 'phone': phone})


def phone_delete(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('products')
    return render(request, 'home/phone_delete.html', {'phone':phone})

def add_comment(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.phone = phone
        comment.save()
        return redirect('phone_detail', pk=pk)
    return render(request, 'home/add_comment.html', {'form': form, 'phone': phone})





