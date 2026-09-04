from django.urls import path
from . import views

urlpatterns = [
    path('', views.tables, name='tables'),
    path('personas/', views.personas, name='personas'),
]