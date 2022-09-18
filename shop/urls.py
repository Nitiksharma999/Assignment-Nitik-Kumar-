
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shophome"),
    path("about", views.about, name="aboutUs"),
    path("contact", views.contact, name="ContactUs"),
    path("tracker", views.tracker, name="Tracking status"),
    path("search", views.search, name="Search"),
    path("products/<int:myid>", views.productview, name="Productview"),
    path("checkout", views.checkout, name="Checkout"),
]
