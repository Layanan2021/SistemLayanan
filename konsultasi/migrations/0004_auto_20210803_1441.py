# Generated by Django 3.1.3 on 2021-08-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konsultasi', '0003_petugas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petugas',
            old_name='name',
            new_name='nama_lengkap',
        ),
        migrations.RemoveField(
            model_name='petugas',
            name='phone',
        ),
        migrations.AddField(
            model_name='petugas',
            name='Jenis_kelamin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='petugas',
            name='alamat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
