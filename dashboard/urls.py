from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ewc', views.ewc),
    path('multi_form/', views.multi_form_view, name='multi_form'),
]