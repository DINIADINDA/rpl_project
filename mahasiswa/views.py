from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Mahasiswa

@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()

    return render(
        request,
        'mahasiswa/daftar.html',
        {'mahasiswas': mahasiswas}
    )