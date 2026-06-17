from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mahasiswa, Buku  # Tambahkan import Buku di sini
from .forms import BukuForm          # Kita akan membuat file forms.py setelah ini

@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(
        request,
        'mahasiswa/daftar.html',
        {'mahasiswas': mahasiswas}
    )

# ==================== KODE BARU UNTUK CRUD BUKU ====================

# 1. Menampilkan Daftar Buku
@login_required(login_url='/accounts/login/')
def daftar_buku(request):
    list_buku = Buku.objects.all()
    return render(
        request, 
        'mahasiswa/daftar_buku.html', 
        {'list_buku': list_buku}
    )

# 2. Tambah Buku Baru
@login_required(login_url='/accounts/login/')
def tambah_buku(request):
    if request.method == 'POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_buku')
    else:
        form = BukuForm()
    
    return render(
        request, 
        'mahasiswa/form_buku.html', 
        {'form': form, 'title': 'Tambah Buku Baru'}
    )

# 3. Edit Data Buku
@login_required(login_url='/accounts/login/')
def edit_buku(request, pk):
    buku = get_object_or_404(Buku, pk=pk)
    if request.method == 'POST':
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            return redirect('daftar_buku')
    else:
        form = BukuForm(instance=buku)
    
    return render(
        request, 
        'mahasiswa/form_buku.html', 
        {'form': form, 'title': 'Edit Data Buku'}
    )

# 4. Hapus Buku
@login_required(login_url='/accounts/login/')
def hapus_buku(request, pk):
    buku = get_object_or_404(Buku, pk=pk)
    if request.method == 'POST':
        buku.delete()
        return redirect('daftar_buku')
    
    return render(
        request, 
        'mahasiswa/hapus_buku.html', 
        {'buku': buku}
    )