from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('pelanggaran/', views.pelanggaran),
    path('siswa/', views.siswa),
    path('pengajar/', views.pengajar),
]