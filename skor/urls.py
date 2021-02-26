from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    path('', views.home, name='home'),
    path('user/', views.userPage, name='user-page'),
    path('akun/', views.akunSetting, name='akun'),
    path('pelanggaran/', views.pelanggaran, name='pelanggaran'),
    path('siswa/<str:pk>/', views.siswa, name='siswa'),
    path('pengajar/<str:pk>/', views.pengajar, name='pengajar'),

    path('buat_pelanggaran/<str:pk>/', views.buatPelanggaran, name='buat_pelanggaran'),
    path('ubah_pelanggaran/<str:pk>/', views.ubahPelanggaran, name='ubah_pelanggaran'),
    path('hapus_pelanggaran/<str:pk>/', views.hapusPelanggaran, name='hapus_pelanggaran'),

    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]