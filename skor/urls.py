from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('pelanggaran/', views.pelanggaran),
    path('murid/', views.murid),
    path('guru/', views.guru),
]