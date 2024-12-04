
from django.urls import path
from . import views

urlpatterns = [
    path('print/',views.print_hello),
    path('home/',views.home_page),
    path("data/",views.get_data),
    path("save-data/",views.save_data),
    path("sud/<int:pk>/",views.single_user_data),
]
