from django.urls import path
from Phone_shop import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("stores/", stores, name="stores"),
    path("customer/", customer, name="customer"),
    path('store/<int:store_id>/', store_detail_view, name='store_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)