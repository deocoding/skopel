from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib import messages

from .models import *
from .forms import PelanggaranForm, BuatUserForm, PengajarForm
from .filters import PelanggaranFilter

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .decorators import *

from django.contrib.auth.models import Group

@unauthenticated_user
def registerPage(request):
    form = BuatUserForm() 
    if request.method == "POST":
        form = BuatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'User "' + username + '" berhasil dibuat')
            return redirect('login')
            
    context = {
        'form': form
    }
    return render(request, 'skor/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'skor/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    pengajars = Pengajar.objects.all()
    pelanggarans = Pelanggaran.objects.all()

    total_pengajar = pengajars.count()

    total_pelanggaran = pelanggarans.count()
    verifikasi = pelanggarans.filter(status='Verifikasi').count()
    terbukti = pelanggarans.filter(status='Terbukti').count()
    tidak_terbukti = pelanggarans.filter(status='Tidak Terbukti').count()

    context = {
        'pengajars': pengajars,
        'pelanggarans': pelanggarans, 
        'total_pengajar': total_pengajar,
        'total_pelanggaran': total_pelanggaran,
        'verifikasi': verifikasi,
        'terbukti': terbukti,
        'tidak_terbukti': tidak_terbukti
    }

    return render(request, 'skor/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['pengajar'])
def userPage(request):
    laporans = request.user.pengajar.pelanggaran_set.all()

    total_pelanggaran = laporans.count()
    verifikasi = laporans.filter(status='Verifikasi').count()
    terbukti = laporans.filter(status='Terbukti').count()
    tidak_terbukti = laporans.filter(status='Tidak Terbukti').count()

    context = {
        'laporans': laporans,
        'total_pelanggaran': total_pelanggaran,
        'verifikasi': verifikasi,
        'terbukti': terbukti,
        'tidak_terbukti': tidak_terbukti
    }
    return render(request, 'skor/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['pengajar'])
def akunSetting(request):
    pengajar = request.user.pengajar
    form = PengajarForm(instance=pengajar)

    if request.method == "POST":
        form = PengajarForm(request.POST, request.FILES, instance=pengajar)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'skor/akun.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pelanggaran(request):
    pasals = Pasal.objects.all()
    context = {
        'pasals': pasals
    }
    return render(request, 'skor/pelanggaran.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def siswa(request, pk):
    siswa = Siswa.objects.get(id=pk)
    pelanggarans = siswa.pelanggaran_set.all()
    total_pelanggaran = pelanggarans.count()
    context = {
        'siswa': siswa,
        'pelanggarans': pelanggarans,
        'total_pelanggaran': total_pelanggaran
    }
    return render(request, 'skor/siswa.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pengajar(request, pk):
    pengajar = Pengajar.objects.get(id=pk)
    laporans = pengajar.pelanggaran_set.all()
    total_laporan = laporans.count()

    myFilter = PelanggaranFilter(request.GET, queryset=laporans)
    laporans = myFilter.qs

    context = {
        'pengajar': pengajar,
        'laporans': laporans,
        'total_laporan': total_laporan,
        'myFilter': myFilter
    }
    
    return render(request, 'skor/pengajar.html', context)

@login_required(login_url='login')
def buatPelanggaran(request, pk):
    PelanggaranFormSet = inlineformset_factory(Pengajar, Pelanggaran, fields=('siswa', 'pasal', 'status'), extra=5)
    pengajar = Pengajar.objects.get(id=pk)
    formset = PelanggaranFormSet(queryset=Pelanggaran.objects.none(), instance=pengajar)
    # form = PelanggaranForm(initial={'pengajar':pengajar})
    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        # form = PelanggaranForm(request.POST)
        formset = PelanggaranFormSet(request.POST, instance=pengajar)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    
    context = {
        'formset': formset
    }

    return render(request, 'skor/pelanggaran_form.html', context)

@login_required(login_url='login')
def ubahPelanggaran(request, pk):
    pelanggaran = Pelanggaran.objects.get(id=pk)    
    form = PelanggaranForm(instance=pelanggaran)

    if request.method == 'POST':
        # print('Printing POST: ', request.POST)
        form = PelanggaranForm(request.POST, instance=pelanggaran)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
        'pelanggaran': pelanggaran
    }

    return render(request, 'skor/pelanggaran_form.html', context)

@login_required(login_url='login')
def hapusPelanggaran(request, pk):
    pelanggaran = Pelanggaran.objects.get(id=pk)
    if request.method == 'POST':
        pelanggaran.delete()
        return redirect('/')
    
    context = {
        'pelanggaran': pelanggaran
    }
    return render(request, 'skor/hapus.html', context)