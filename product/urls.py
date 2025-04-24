from django.urls import path

from product import views

urlpatterns = [
    path("product/", views.index), # index url
    path("product/add", views.index),

]