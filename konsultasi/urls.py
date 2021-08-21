from django.urls import path 
from . import views

urlpatterns = [
    path('home_page', views.home_page, name='home_page'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    
    path('petugas/', views.petugasPage, name='petugas'),
    path('createpetugas/', views.createpetugasPage, name='createpetugas'),
    path('masyarakat/', views.masyarakatPage, name='masyarakat'),
    path('pakar/', views.pakarPage, name='pakar'),
    path('createpakar/', views.createpakarPage, name='createpakar'),
    path('createmasyarakat/', views.createmasyarakatPage, name='createmasyarakat'),
    path('updatepetugas/<str:pk>', views.updatepetugasPage, name='updatepetugas'),
    path('deletepetugas/<str:pk>', views.deletePetugasPage, name='deletepetugas'),
    path('updatepakar/<str:pk>', views.updatepakarPage, name='updatepakar'),
    path('deletepakar/<str:pk>', views.deletePakarPage, name='deletepakar'),
    path('updatemasyarakat/<str:pk>', views.updatemasyarakatPage, name='updatemasyarakat'),
    path('deletemasyarakat/<str:pk>', views.deleteMasyarakatPage, name='deletemasyarakat'),

    # kosultasi chat SendView
    path('konsultasi/', views.konsultasi_page, name='konsultasi'),
    path('send/', views.SendView, name='send'),
    path('hapuschat/<str:idpk>', views.hapusbebas, name='hapuschat'),

    # religius hapusreligius
    path('religius/', views.relegius_page, name='religius'),
    path('hapusR/<str:idpk>', views.hapusreligius, name='hapusR'),

    # laporan
    path('lp_ms/', views.LP_masyarakat, name='lp_ms'),
    path('lp_PK/', views.LP_pakar, name='lp_PK'),
]
