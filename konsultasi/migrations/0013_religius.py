# Generated by Django 3.1.3 on 2021-08-18 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konsultasi', '0012_auto_20210818_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='religius',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_konsultasi', models.CharField(blank=True, max_length=50, null=True)),
                ('id_pengguna', models.CharField(blank=True, max_length=200, null=True)),
                ('judul', models.CharField(blank=True, max_length=200, null=True)),
                ('tanggal', models.DateTimeField(auto_now_add=True, null=True)),
                ('jam', models.TimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
