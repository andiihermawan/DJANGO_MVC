# Generated by Django 2.1.5 on 2019-02-11 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_challenge', models.CharField(max_length=50)),
                ('banyak_soal', models.CharField(max_length=3)),
                ('bobot_nilai', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Direksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=50)),
                ('no_telepon', models.CharField(max_length=15)),
                ('jabatan', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Live_Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_Live_Code', models.CharField(max_length=50)),
                ('banyak_soal', models.CharField(max_length=3)),
                ('bobot_nilai', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Mata_pelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelajaran', models.CharField(max_length=50)),
                ('jadwal_dimulai', models.CharField(max_length=50)),
                ('adwal_berakhir', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=50)),
                ('no_telepon', models.CharField(max_length=15)),
                ('no_absen', models.CharField(max_length=3)),
                ('nilai_rata_rata', models.FloatField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=50)),
                ('no_telepon', models.CharField(max_length=15)),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ATA.Mata_pelajaran')),
            ],
        ),
        migrations.AddField(
            model_name='live_code',
            name='tangal_pelaksanaan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ATA.Mata_pelajaran'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='mata_pelajaran',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ATA.Mata_pelajaran'),
        ),
    ]
