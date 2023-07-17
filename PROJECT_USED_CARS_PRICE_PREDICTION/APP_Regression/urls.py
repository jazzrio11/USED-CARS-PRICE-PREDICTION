from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('home', views.home),
    # path("regression",views.new),
    # path("add",views.add),
    # path("selection_form",views.selection_form),
    # path("show",views.show),
    path("",views.index),
    path("predict_price",views.predict_price),
]
