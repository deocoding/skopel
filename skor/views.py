from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .models import *
from .forms import PelanggaranForm
from .filters import PelanggaranFilter

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

def pelanggaran(request):
    pasals = Pasal.objects.all()
    context = {
        'pasals': pasals
    }
    return render(request, 'skor/pelanggaran.html', context)

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

def hapusPelanggaran(request, pk):
    pelanggaran = Pelanggaran.objects.get(id=pk)
    if request.method == 'POST':
        pelanggaran.delete()
        return redirect('/')
    
    context = {
        'pelanggaran': pelanggaran
    }
    return render(request, 'skor/hapus.html', context)