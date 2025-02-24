from itertools import product

from django.urls import path
from django.conf.urls.static import static
from Phone_shop import settings
from .views import *

urlpatterns = [
    path("", body, name="body"),
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("products/", products, name="products"),
    path("phone/<int:pk>/", phone_detail, name="phone_detail"),
    path("phone-list/", phone_list, name="phone_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
