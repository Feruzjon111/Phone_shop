from django.urls import path
from django.conf.urls.static import static
from Phone_shop import settings
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("products/", PhoneListView.as_view() , name="products"),
    path("phone/<int:pk>/", PhoneDetailView.as_view() , name="phone_detail"),
    path("phone_create/", PhoneCreateView.as_view() , name="phone_create"),
    path("phone/phone_update/<int:pk>/", PhoneUpdateView.as_view() , name="phone_update"),
    path("phone_delete/<int:pk>/", PhoneDeleteView.as_view() , name="phone_delete"),
    path('phone/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
