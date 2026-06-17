from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='daftar/')),
    path('daftar/', views.daftar_mahasiswa, name='daftar_mahasiswa'),

    path('buku/', views.daftar_buku, name='daftar_buku'),
    path('buku/tambah/', views.tambah_buku, name='tambah_buku'),
    path('buku/edit/<int:pk>/', views.edit_buku, name='edit_buku'),
    path('buku/hapus/<int:pk>/', views.hapus_buku, name='hapus_buku'),
]