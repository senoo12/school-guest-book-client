from django.shortcuts import render, redirect
from django.views import View
from guest.models import *

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class FormView(View):
    def get(self, request):
        return render(request, 'form.html')
    def post(self, request):
        if request.method == "POST":
            name = request.POST['name']
            jenis_kelamin = request.POST['jenis_kelamin']
            kategori_dituju = request.POST['kategori_dituju']
            pihak_dituju = request.POST['pihak_dituju']
            keperluan = request.POST['keperluan']
            no_hp = request.POST['no_hp']
            foto = request.FILES.get('foto')
            obj=Guest.objects.create(name=name, jenis_kelamin=jenis_kelamin, kategori_dituju=kategori_dituju, pihak_dituju=pihak_dituju, keperluan=keperluan, no_hp=no_hp, foto=foto)
        obj.save()
        return redirect('../form/')
