from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard-berita/', views.dashboardBerita, name='dashboard-berita'),
    path('dashboard-artikel/', views.dashboardArtikel, name='dashboard-artikel'),
    path('dashboard-contact/', views.dashboardContact, name='dashboard-contact'),
    path('osis/', views.osis, name='osis'),

    path('profil-berita/<str:pk>/', views.berita, name='profil-berita'),
    path('input-berita/', views.inputBerita, name='input-berita'),
    path('search-berita/', views.searchBerita, name='search-berita'),
    path('lihat-berita/', views.lihatBerita, name='lihat-berita'),    
    path('list-berita/', views.listBerita, name='list-berita'),
    path('process_berita/', views.processBerita, name='process_berita'),
    path('comment_berita/', views.commentBerita, name='comment_berita'),
    path('delete_berita/<str:pk>/', views.deleteBerita, name='delete_berita'),
    
    path('profil-artikel/<str:pk>/', views.artikel, name='profil-artikel'),
    path('list-artikel/', views.listArtikel, name='list-artikel'),
    path('lihat-artikel/', views.lihatArtikel, name='lihat-artikel'),
    path('input-artikel/', views.inputArtikel, name='input-artikel'),
    path('search-artikel/', views.searchArtikel, name='search-artikel'),
    path('process_artikel/', views.processArtikel, name='process_artikel'),
    path('delete_artikel/<str:pk>/', views.deleteArtikel, name='delete_artikel'),

    path('contact/', views.contact, name='contact'),
    path('input-contact/', views.inputContact, name='input-contact'),
    path('lihat-contact/', views.lihatContact, name='lihat-contact'),
    path('delete_contact/<str:pk>/', views.deleteContact, name='delete_contact'),
]
