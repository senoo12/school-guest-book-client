from django.contrib import admin
from guest.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class GuestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name', 'jenis_kelamin', 'kategori_dituju', 'pihak_dituju', 'keperluan', 'no_hp', 'foto')
    readonly_fields = ("created_at", "updated_at",)
    list_filter = ["created_at", "jenis_kelamin", "kategori_dituju", "pihak_dituju",]

admin.site.register(Guest, GuestAdmin)