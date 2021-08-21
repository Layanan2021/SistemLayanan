# Generated by Django 3.1.3 on 2021-08-03 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konsultasi', '0004_auto_20210803_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masyarakat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(blank=True, max_length=200, null=True)),
                ('alamat', models.CharField(blank=True, max_length=200, null=True)),
                ('Jenis_kelamin', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pakar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(blank=True, max_length=200, null=True)),
                ('alamat', models.CharField(blank=True, max_length=200, null=True)),
                ('Jenis_kelamin', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='petugas',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]