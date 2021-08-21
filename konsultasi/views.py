
from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import *
from .forms import PetugasForm, PakarForm, MasyarakatForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import tolakhalaman_ini, ijinkan_pengguna
# from django.contrib.auth.models import Group


# @ijinkan_pengguna(yang_diizinkan=['azizah'])
@login_required(login_url='login')
def home_page(request):
    list_petugas = Petugas.objects.all()
    list_masyarakat = Masyarakat.objects.all()
    list_pakar = Pakar.objects.all()
    context = {
        'judul': 'Halaman Beranda',
        'Petugas':list_petugas,
        'Masyarakat':list_masyarakat,
        'Pakar':list_pakar,
    }

    return render(request, 'konsultasi/index.html', context)




def loginPage (request):
    login = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        cocokan = authenticate(request, username=username, password=password )
        if cocokan is not None:
            login(request, cocokan)
            return redirect('home_page')
    
    context = {
        'judul': 'Halaman Login',
        'menu': 'login',
        'tampillogin' : login
        
        
    }

    return render(request, 'konsultasi/login.html', context)

@tolakhalaman_ini
def registerPage (request):
    if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password')
            password2 = request.POST.get('password2')
            if  username == "" :
                messages.success(request, 'Username belum di isi.')
                return redirect('register')
                if User.objects.filter(username = username).first():
                     messages.success(request, 'Username sudah ada.')
                     return redirect('register')
                     if email == "" :
                         messages.success(request, 'Email Belum diisi')
                         return redirect('register')
                         if password1 == "" :
                              messages.success(request, 'Password belum')
                              return redirect('register')
                              if password1 != password2:
                                   messages.success(request, 'Password Tidak sama')
                                   return redirect('register')
                                   user = User.objects.create_user(username=username, email=email)
                                   user.set_password(password1)
                                   user.is_active = True
                                   user.save()
                                   return redirect('login')

    context = {
        'judul': 'Halaman Register',
        'menu': 'register',
        
    
    }
    
    return render(request, 'konsultasi/register.html', context)


def petugasPage (request):
    list_petugas = Petugas.objects.all()
    
 
    context = {
        'judul': 'Halaman Petugas',
        'Petugas':list_petugas,
    }

    return render(request, 'konsultasi/petugas.html', context)


def masyarakatPage (request):
    list_masyarakat = Masyarakat.objects.all()
    
 
    context = {
        'judul': 'Halaman Masyarakat',
        'Masyarakat':list_masyarakat,
    }

    return render(request, 'konsultasi/masyarakat.html', context)


def pakarPage (request):
    list_pakar = Pakar.objects.all()
    
 
    context = {
        'judul': 'Halaman Masyarakat',
        'Pakar':list_pakar,
    }

    return render(request, 'konsultasi/pakar.html', context)


def createpetugasPage (request):
    formpetugas = PetugasForm()
    if request.method == 'POST':
        #print('Cetak POST:', request.POST)
        formsimpan = PetugasForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('petugas')
    context = {
        'judul': 'Halaman input',
        'form' : formpetugas, 
    }

    return render(request, 'konsultasi/createpetugas.html', context)



def createpakarPage (request):
    formpakar = PakarForm()
    if request.method == 'POST':
        #print('Cetak POST:', request.POST)
        formsimpan = PakarForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('pakar')
    context = {
        'judul': 'Halaman input',
        'form' : formpakar, 
    }

    return render(request, 'konsultasi/createpakar.html', context)


def createmasyarakatPage (request):
    formmasyarakat = MasyarakatForm()
    if request.method == 'POST':
        #print('Cetak POST:', request.POST)
        formsimpan = MasyarakatForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('masyarakat')
    context = {
        'judul': 'Halaman input',
        'form' : formmasyarakat, 
    }

    return render(request, 'konsultasi/createmasyarakat.html', context)



def updatepetugasPage(request, pk):
    up_petugas = Petugas.objects.get(id=pk)
    formpetugas = PetugasForm(instance=up_petugas)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = PetugasForm(request.POST, request.FILES, instance=up_petugas)
        if formedit.is_valid:
            formedit.save()
            return redirect('petugas')
    context = {
        'judul': 'Edit Order',
        'form' : formpetugas, 
    }
    return render(request, 'konsultasi/updatepetugas.html', context)


def deletePetugasPage(request, pk):
    petugashapus = Petugas.objects.get(id=pk)
    if request.method == 'POST':
        petugashapus.delete()
        return redirect('petugas')
    context = {
        'judul': 'Hapus Data Petugas',
        'datapetugasdelete' : petugashapus, 
 }
    return render(request, 'konsultasi/deletepetugas.html', context)


def updatepakarPage(request, pk):
    up_pakar = Pakar.objects.get(id=pk)
    formpakar = PakarForm(instance=up_pakar)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = PakarForm(request.POST, request.FILES, instance=up_pakar)
        if formedit.is_valid:
            formedit.save()
            return redirect('pakar')
    context = {
        'judul': 'Edit Order',
        'form' : formpakar, 
    }
    return render(request, 'konsultasi/updatepakar.html', context)

def deletePakarPage(request, pk):
    Pakar.objects.filter(id=pk).delete()
    return redirect('pakar') 

# def deletePakarPage(request, pk):
#     pakarhapus = Pakar.objects.get(id=pk)
#     if request.method == 'POST':
#         pakarhapus.delete()
#         return redirect('pakar')
#     context = {
#         'judul': 'Hapus Data Pakar',
#         'datapakardelete' : pakarhapus, 
#  }
#     return render(request, 'konsultasi/deletepakar.html', context)


def updatemasyarakatPage(request, pk):
    up_masyarakat = Masyarakat.objects.get(id=pk)
    formmasyarakat = MasyarakatForm(instance=up_masyarakat)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = MasyarakatForm(request.POST, request.FILES, instance=up_masyarakat)
        if formedit.is_valid:
            formedit.save()
            return redirect('masyarakat')
    context = {
        'judul': 'Edit Order',
        'form' : formmasyarakat, 
    }
    return render(request, 'konsultasi/updatemasyarakat.html', context)


def deleteMasyarakatPage(request, pk):
    masyarakathapus = Masyarakat.objects.get(id=pk)
    if request.method == 'POST':
        masyarakathapus.delete()
        return redirect('masyarakat')
    context = {
        'judul': 'Hapus Data Masyarakat',
        'datamasyarakatdelete' : masyarakathapus, 
 }
    return render(request, 'konsultasi/deletemasyarakat.html', context)


# laporan 
def LP_masyarakat (request):
    LP_MS = Masyarakat.objects.all()
    context = {
        'judul': 'Halaman Masyarakat',
        'LP_MS':LP_MS,
    }

    return render(request, 'konsultasi/Laporan/lp_masyarakat.html', context)

def LP_pakar (request):
    LP_pakar = Pakar.objects.all()
    context = {
        'judul': 'Halaman Masyarakat',
        'LP_pakar':LP_pakar,
    }

    return render(request, 'konsultasi/Laporan/lp_pakar.html', context)


# konsultasi
def konsultasi_page(request):
    chat_konsul = chat.objects.all()
    context = {
        'judul': 'Halaman Konsultasi',
        'chat_konsul': chat_konsul
    }

    return render(request, 'konsultasi/Konsultasi/konsultasi.html', context)

def SendView(request):
    if request.method == 'POST':
        chat.objects.create(
            id_pesan = request.POST['idps'],
            id_konsultasi = request.POST['idk'],
            id_pengguna = request.POST['idpg'],
            petugas = request.POST['idpt'],
            isi = request.POST['isi'],
            )
        return redirect('konsultasi')
        
    context = {
    'page_title':'send data',
    
    }
    return render(request, 'konsultasi/Konsultasi/konsultasi.html', context)

def hapusbebas(request, idpk):
    chat.objects.filter(id=idpk).delete()
    return redirect('konsultasi')  

    # relegius
def relegius_page(request):
    religius1 = religius.objects.all()
    context = {
        'judul': 'Halaman Konsultasi',
        'religius1': religius1
    }

    return render(request, 'konsultasi/Konsultasi/k_religius.html', context)

def hapusreligius(request, idpk):
    religius.objects.filter(id=idpk).delete()
    return redirect('religius')  