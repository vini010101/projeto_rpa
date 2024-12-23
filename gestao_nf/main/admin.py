from django.contrib import admin
from main.models import Usuarios, NotaFiscal, UploadNotaFiscal

# Register your models here.
admin.site.register(Usuarios),
admin.site.register(NotaFiscal),
admin.site.register(UploadNotaFiscal)