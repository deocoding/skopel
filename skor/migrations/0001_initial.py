# Generated by Django 2.2.18 on 2021-02-22 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Kelas',
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
                'verbose_name_plural': 'Pasal',
            },
        ),
        migrations.CreateModel(
            name='Pengajar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('nip', models.CharField(max_length=200, null=True)),
                ('jabatan', models.CharField(choices=[('Kepala Sekolah', 'Kepala Sekolah'), ('Wakil Kepala Sekolah Bidang Kesiswaan', 'Wakil Kepala Sekolah Bidang Kesiswaan'), ('Pembina Osis', 'Pembina Osis'), ('Guru Kelas', 'Guru Kelas'), ('Guru BK', 'Guru BK')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pengajar',
            },
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('nisn', models.CharField(max_length=200, null=True)),
                ('ibu', models.CharField(blank=True, max_length=200, null=True)),
                ('ayah', models.CharField(blank=True, max_length=200, null=True)),
                ('wali', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('kelas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='skor.Kelas')),
            ],
            options={
                'verbose_name_plural': 'Siswa',
            },
        ),
        migrations.CreateModel(
            name='Pelanggaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Verifikasi', 'Verifikasi'), ('Terbukti', 'Terbukti')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('pasal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='skor.Pasal')),
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