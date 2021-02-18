from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('pelanggarans/', views.pelanggarans),
    path('murid/', views.murid),
    path('guru/', views.guru),
]