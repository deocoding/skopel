from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'skor/dashboard.html')

def pelanggaran(request):
    return render(request, 'skor/pelanggaran.html')

def siswa(request):
    return render(request, 'skor/siswa.html')

def pengajar(request):
    return render(request, 'skor/pengajar.html')
