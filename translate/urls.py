from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='translate.index'),
    path('translate/', views.show, name='translate.show'),
]
