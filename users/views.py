from django.shortcuts import render, get_object_or_404

from users.models import Customers, Stores


def stores(request):
    stores = Stores.objects.all()
    context = {'stores':stores}
    return render(request, 'users/stores.html', context)

def customer(request):
    customers = Customers.objects.all()
    context = {'customers':customers}
    return render(request, 'users/customer.html', context)

def store_detail_view(request, store_id):
    store = get_object_or_404(Stores, id=store_id)
    return render(request, 'users/store_detail.html', {'store': store})