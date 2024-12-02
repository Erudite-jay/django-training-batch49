
from django.urls import path
from . import views

urlpatterns = [
    path('print/',views.print_hello),
    path('home/',views.home_page),
]
