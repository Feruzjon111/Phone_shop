from django.urls import path
from django.conf.urls.static import static
from Phone_shop import settings
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("products/", products, name="products"),
    path("phone/<int:pk>/", phone_detail, name="phone_detail"),
    path("phone_create/", phone_create, name="phone_create"),
    path("phone/phone_update/<int:pk>/", phone_update, name="phone_update"),
    path("phone_delete/<int:pk>/", phone_delete, name="phone_delete"),
    path('phone/<int:pk>/comment/', add_comment, name='add_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
