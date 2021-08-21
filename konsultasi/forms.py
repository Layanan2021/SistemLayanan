from django import forms
from django.forms import ModelForm
from .models import Petugas, Pakar, Masyarakat



class PetugasForm(ModelForm):
    class Meta:
        model = Petugas
        fields= '__all__'
        widgets = {
            'nik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIK', 'size': '100'}),
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Petugas', 'size': '100'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alamat', 'size': '100'}),
            'Jenis_kelamin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jenis Kelamin', 'size': '100'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'No Telepon', 'type': 'number', 'size': '100'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Petugas', 'size': '100'}),
        }
        labels = {
            'nik': 'Nik',
            'nama_lengkap': 'Nama Petugas',
            'alamat': 'Alamat Petugas',
            'Jenis_kelamin': 'Jenis Kelamin',
            'phone': 'No Telepon',
            'email': 'Email',
        }

class PakarForm(ModelForm):
    class Meta:
        model = Pakar
        fields= '__all__'
        widgets = {
            'id_pengguna': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'id pengguna', 'type': 'number', 'size': '100'}),
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Pakar', 'size': '100'}),
            'Jenis_kelamin': forms.Select(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alamat', 'size': '100'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Pakar', 'size': '100'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'size': '100'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'size': '100'}),
            
        }
        labels = {
            'id_pengguna' : 'id pengguna',
            'nama_lengkap' : 'Nama Pakar',
            'Jenis_kelamin': 'Jenis Kelamin',
            'alamat': 'Alamat Pakar',
            'email': 'Email',
            'username': 'username',
            'password': 'password',
            
            
        }

class MasyarakatForm(ModelForm):
    class Meta:
        model = Masyarakat
        fields= '__all__'
        widgets = {
            'id_pengguna': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'id pengguna', 'type': 'number', 'size': '100'}),
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Masyarakat', 'size': '100'}),
            'Jenis_kelamin': forms.Select(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alamat', 'size': '100'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Masyarakat', 'size': '100'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'size': '100'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'size': '100'}),
            
        }
        labels = {
            'id_pengguna' : 'id pengguna',
            'nama_lengkap' : 'Nama Masyarakat',
            'Jenis_kelamin': 'Jenis Kelamin',
            'alamat': 'Alamat Masyarakat',
            'email': 'Email',
            'username': 'username',
            'password': 'password',
            
            
        }




