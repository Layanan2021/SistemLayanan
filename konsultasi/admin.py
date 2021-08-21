from django.contrib import admin

# Register your models here. konsultasi_chat
from .models import *
admin.site.register(Petugas)
admin.site.register(Pakar)
admin.site.register(Masyarakat)
admin.site.register(chat)
admin.site.register(religius)


def __str__(self):
 return self.nama_lengkap