# Generated by Django 2.2.19 on 2021-02-26 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': '      Jabatan',
            },
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': '   Kelas',
            },
        ),
        migrations.CreateModel(
            name='Pasal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True, unique=True)),
                ('jenis', models.CharField(max_length=200, null=True, unique=True)),
                ('skor', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': ' Pasal',
            },
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('nisn', models.CharField(max_length=200, null=True)),
                ('kelamin', models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=200, null=True)),
                ('kelas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='skor.Kelas')),
            ],
            options={
                'verbose_name_plural': '  Siswa',
            },
        ),
        migrations.CreateModel(
            name='Pengajar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('nip', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('PNS', 'PNS'), ('Guru Tidak Tetap', 'Guru Tidak Tetap'), ('Guru Honorer', 'Guru Honorer'), ('Lainnya', 'Lainnya')], max_length=200, null=True)),
                ('foto_profil', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('jabatan', models.ManyToManyField(to='skor.Jabatan')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '    Pengajar',
            },
        ),
        migrations.CreateModel(
            name='Pelanggaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Verifikasi', 'Verifikasi'), ('Terbukti', 'Terbukti'), ('Tidak Terbukti', 'Tidak Terbukti')], max_length=200, null=True)),
                ('keterangan', models.CharField(max_length=1000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('pasal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='skor.Pasal')),
                ('pengajar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='skor.Pengajar')),
                ('siswa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='skor.Siswa')),
            ],
            options={
                'verbose_name_plural': 'Pelanggaran',
            },
        ),
        migrations.AddField(
            model_name='kelas',
            name='bk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bk', to='skor.Pengajar'),
        ),
        migrations.AddField(
            model_name='kelas',
            name='wali',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wali', to='skor.Pengajar'),
        ),
    ]
