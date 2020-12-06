from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
import markdown

from .models import *
from .forms import ContactForm
from .filters import BeritaFilter, ArtikelFilter, ContactFilter
from .decorators import unauthenticated_user

# Create your views here.


##################################################   Wilayah Login
@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR Password Incorrect')



    context = {}
    return render(request, 'coreApp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')
#################################################################################

@login_required(login_url='login')
def dashboard(request):

    berita = Berita.objects.count() 
    artikel = Artikel.objects.count()
    contact = Contact.objects.count()   

    context = {'berita':berita, 'artikel':artikel, 'contact':contact}
    return render(request, 'coreApp/dashboard-main.html', context)

@login_required(login_url='login')
def dashboardBerita(request):

    berita = Berita.objects.all()
    
    context = {'berita':berita}
    return render(request, 'coreApp/dashboard-berita.html', context)

@login_required(login_url='login')
def dashboardArtikel(request):

    context = {}
    return render(request, 'coreApp/dashboard-artikel.html', context)

@login_required(login_url='login')
def dashboardContact(request):

    context = {}
    return render(request, 'coreApp/dashboard-contact.html', context)


def home(request):

    berita = Berita.objects.all()

    berita_list = list(berita)
    bertia_r = berita_list[::-1]
    berita_5 = bertia_r[:3]

    artikel = Artikel.objects.all()
    artikel_list = list(artikel)
    artikel_r = artikel_list[::-1]
    artike_5 = artikel_r[:3]

    context = {'berita_5':berita_5, 'artikel_5':artike_5}
    return render(request, 'coreApp/home.html', context)

def osis(request):

    context = {}
    return render(request, 'coreApp/osis.html', context)


############################################# Wilayah Berita
def berita(request, pk):

    berita = Berita.objects.get(id=pk)
    format_text = markdown.markdown(berita.isi_berita) 

    commentar = berita.comment_set.all()

    context = {'berita':berita, 'format_text':format_text, 'commentar':commentar}
    return render(request, 'coreApp/berita.html', context)

def listBerita(request):

    beritas = Berita.objects.all()

    context = {'beritas':beritas}
    return render(request, 'coreApp/listBerita.html', context)

@login_required(login_url='login')
def inputBerita(request):

    context = {}
    return render(request, 'coreApp/berita-input.html', context)

@login_required(login_url='login')
def searchBerita(request):

    berita = Berita.objects.all()

    myfilter = BeritaFilter(request.GET, queryset=berita)
    berita_filter = myfilter.qs

    context = {'berita':berita, 'myfilter':myfilter, 'berita_filter':berita_filter}
    return render(request, 'coreApp/berita-search.html', context)

@login_required(login_url='login')
def lihatBerita(request):

    berita = Berita.objects.all()

    context = {'berita':berita}
    return render(request, 'coreApp/berita-lihat.html', context)

@login_required(login_url='login')
def processBerita(request):

    data = json.loads(request.body)

    Berita.objects.create(
        judul_berita = data['form']['judul'],
        short_line = data['form']['shortLine'],
        isi_berita = data['form']['isiBerita'],
        note = data['form']['note'],
    )    

    return JsonResponse('Input Complete', safe=False)

@login_required(login_url='login')
def deleteBerita(request, pk):

    berita = Berita.objects.get(id=pk)

    if request.method == 'POST':
        berita.delete()
        return redirect('lihat-berita')
    
    context = {'berita':berita}
    return render(request, 'coreApp/berita-delete.html', context)

def commentBerita(request):

    data = json.loads(request.body) 

    berita= Berita.objects.get(id=data['form']['idBerita'])

    Comment.objects.create(
        berita = berita,
        nama= data['form']['nama'],
        jurusan= data['form']['jurusan'],
        commentar= data['form']['commentar'],
    )


    return JsonResponse('Input commentar Success', safe=False)

########################################################################
#########################################################  Wilayah Artikel


def artikel(request, pk):

    artikel = Artikel.objects.get(id=pk)

    context = {'artikel':artikel}
    return render(request, 'coreApp/artikel.html', context)

def listArtikel(request):
    
    artikel = Artikel.objects.all()

    context = {'artikel':artikel}
    return render(request, 'coreApp/listArtikel.html', context)

@login_required(login_url='login')
def inputArtikel(request):
    
    context = {}
    return render(request, 'coreApp/artikel-input.html', context)

@login_required(login_url='login')
def lihatArtikel(request):
    
    artikel = Artikel.objects.all()

    context = {'artikel':artikel}
    return render(request, 'coreApp/artikel-lihat.html', context)

@login_required(login_url='login')
def searchArtikel(request):
    
    artikel = Artikel.objects.all()

    myfilter = ArtikelFilter(request.GET, queryset=artikel)
    artikel_filter = myfilter.qs

    context = {'artikel':artikel, 'myfilter':myfilter, 'artikel_filter':artikel_filter}
    return render(request, 'coreApp/artikel-search.html', context)

@login_required(login_url='login')
def deleteArtikel(request, pk):

    artikel = Artikel.objects.get(id=pk)

    if request.method == 'POST':
        artikel.delete()
        return redirect('lihat-artikel')

    context = {'artikel':artikel}
    return render(request, 'coreApp/artikel-delete.html', context)

@login_required(login_url='login')
def processArtikel(request):

    data = json.loads(request.body)

    Artikel.objects.create(
        tipe = data['form']['tipe'],
        judul_artikel = data['form']['judulArtikel'],
        short_line= data['form']['shortLine'],
        isi_artikel = data['form']['isiArtikel'],
        author = data['form']['author'],
    )

    return JsonResponse('Input Complete', safe=False)


####################################################################################
#################################################  Wilayah Contact
def contact(request):

    contact = Contact.objects.all()

    context = {'contact':contact}
    return render(request, 'coreApp/contact.html', context)

@login_required(login_url='login')
def inputContact(request):
    
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-contact')

    context = {'form':form}
    return render(request, 'coreApp/contact-input.html', context)

@login_required(login_url='login')
def lihatContact(request):

    contact = Contact.objects.all()

    context = {'contact':contact}
    return render(request, 'coreApp/contact-lihat.html', context)

@login_required(login_url='login')
def deleteContact(request, pk):

    contact = Contact.objects.get(id=pk)

    context = {'contact':contact}
    return render(request, 'coreApp/contact-delete.html', context)