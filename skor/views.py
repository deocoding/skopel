from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home(request):
    siswa = Siswa.objects.all()
    pelanggarans = Pelanggaran.objects.all()

    context = {
        'siswa': siswa,
        'pelanggaran': pelanggaran
    }

    return render(request, 'skor/dashboard.html', context)

def pelanggaran(request):
    pasals = Pasal.objects.all()
    context = {
        'pasals': pasals
    }
    return render(request, 'skor/pelanggaran.html', context)

def siswa(request):
    return render(request, 'skor/siswa.html')

def pengajar(request):
    return render(request, 'skor/pengajar.html')
