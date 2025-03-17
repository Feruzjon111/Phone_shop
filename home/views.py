from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import PhoneForm, CommentForm
from .models import Phone, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View

def home(request):
    phones = Phone.objects.all()[:3]
    context = {'phones': phones}
    return render(request, 'home/home.html', context)

# def products(request):
#     phones = Phone.objects.all()
#     context = {'phones': phones}
#     return render(request, 'home/products.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

# def phone_detail(request, pk):
#     phone = get_object_or_404(Phone, id=pk)
#     comments = Comment.objects.filter(phone=phone).order_by('-created_date')
#     context = {'phone': phone, 'comments': comments}
#     return render(request, 'home/phone_detail.html', context)

# def phone_create(request):
#     form = PhoneForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return redirect('products')
#     return render(request, 'home/phone_create.html', {'form': form})


# def phone_update(request, pk):
#     phone = get_object_or_404(Phone, id=pk)
#     if request.method == 'POST':
#         form = PhoneForm(request.POST, request.FILES, instance=phone)
#         if form.is_valid():
#             form.save()
#             return redirect('phone_detail', pk=phone.pk)
#     else:
#         form = PhoneForm(instance=phone)
#     return render(request, 'home/phone_update.html', {'form': form, 'phone': phone})


# def phone_delete(request, pk):
#     phone = get_object_or_404(Phone, id=pk)
#     if request.method == 'POST':
#         phone.delete()
#         return redirect('products')
#     return render(request, 'home/phone_delete.html', {'phone':phone})

# def add_comment(request, pk):
#     phone = get_object_or_404(Phone, id=pk)
#     form = CommentForm(request.POST or None)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.phone = phone
#         comment.save()
#         return redirect('phone_detail', pk=pk)
#     return render(request, 'home/add_comment.html', {'form': form, 'phone': phone})


# class PhoneListView(ListView):
#     model = Phone
#     template_name = 'home/products.html'
#     context_object_name = 'phones'
#     ordering = ['-created_date']
#
#
# class PhoneDetailView(DetailView):
#     model = Phone
#     template_name = 'home/phone_detail.html'
#     context_object_name = 'phone'
#
#
# class PhoneCreateView(CreateView):
#     model = Phone
#     form_class = PhoneForm
#     template_name = 'home/phone_create.html'
#     success_url =  reverse_lazy('products')
#
#
# class PhoneUpdateView(UpdateView):
#     model = Phone
#     form_class = PhoneForm
#     template_name = 'home/phone_update.html'
#     context_object_name = 'phone'
#
#     def get_success_url(self):
#         return reverse_lazy('phone_detail', kwargs={'pk': self.object.pk})
#
#
# class PhoneDeleteView(DeleteView):
#     model = Phone
#     template_name = 'home/phone_delete.html'
#     success_url = reverse_lazy('products')

class PhoneCreateView(View):
    def get(self, request):
        phones = Phone.objects.all()
        context = {'phones': phones}
        return render(request, 'home/phone_create.html', context)

    def post(self, request):
        form = PhoneForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('products')
        return render(request, 'home/phone_create.html', {'form': form})

class PhoneDetailView(View):
    def get(self, request, pk):
        phone = get_object_or_404(Phone, id=pk)
        comments = Comment.objects.filter(phone=phone).order_by('-created_date')
        context = {'phone': phone, 'comments': comments}
        return render(request, 'home/phone_detail.html', context)


class PhoneUpdateView(View):
    def get(self, request, pk):
        phone = get_object_or_404(Phone, id=pk)
        form = PhoneForm(instance=phone)
        context = {'form': form, 'phone': phone}
        return render(request, 'home/phone_update.html', context)

    def post(self, request, pk):
        phone = get_object_or_404(Phone, id=pk)
        form = PhoneForm(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phone_detail', pk=phone.pk)
        return render(request, 'home/phone_update.html', {'form': form, 'phone': phone})


class PhoneDeleteView(View):
    def get(self, request, pk):
        phone = get_object_or_404(Phone, id=pk)
        context = {'phone': phone}
        return render(request, 'home/phone_delete.html', context)

    def post(self, request, pk):
        phone = get_object_or_404(Phone, id=pk)
        phone.delete()
        return redirect('products')

class AddCommentView(View):
    def get(self, request, pk):
        phone = get_object_or_404(Phone, id=pk)
        form = CommentForm()
        context = {'form': form, 'phone': phone}
        return render(request, 'home/add_comment.html', context)

    def post(self, request, pk):
        phone = get_object_or_404(Phone, id=pk)
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.phone = phone
            comment.save()
            return redirect('phone_detail', pk=pk)
        return render(request, 'home/add_comment.html', {'form': form, 'phone': phone})

class PhoneListView(View):
    def get(self, request):
        phones = Phone.objects.all()
        context = {'phones': phones}
        return render(request, 'home/products.html', context)











