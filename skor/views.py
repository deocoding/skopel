from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'skor/dashboard.html')

def pelanggarans(request):
    return render(request, 'skor/pelanggarans.html')

def murid(request):
    return render(request, 'skor/murid.html')

def guru(request):
    return render(request, 'skor/guru.html')
