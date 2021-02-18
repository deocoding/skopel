from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home')

def pelanggarans(request):
    return HttpResponse('Pelanggaran')

def murid(request):
    return HttpResponse('Murid')

def guru(request):
    return HttpResponse('Guru')
