from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('socio/nuevo/', views.create_socio, name='create_socio'),
    path('entrenador/nuevo/', views.create_entrenador, name='create_entrenador'),
    path('clase/nueva/', views.create_clase, name='create_clase'),
    path('buscar/', views.search, name='search'),
]
