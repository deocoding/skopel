from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),

    path('', views.home, name='home'),
    path('pelanggaran/', views.pelanggaran, name='pelanggaran'),
    path('siswa/<str:pk>/', views.siswa, name='siswa'),
    path('pengajar/<str:pk>/', views.pengajar, name='pengajar'),

    path('buat_pelanggaran/<str:pk>/', views.buatPelanggaran, name='buat_pelanggaran'),
    path('ubah_pelanggaran/<str:pk>/', views.ubahPelanggaran, name='ubah_pelanggaran'),
    path('hapus_pelanggaran/<str:pk>/', views.hapusPelanggaran, name='hapus_pelanggaran'),
]