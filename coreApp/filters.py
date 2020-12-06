import django_filters
from django_filters import CharFilter


from .models import *

class BeritaFilter(django_filters.FilterSet):
    judul = CharFilter(field_name = 'judul_berita', lookup_expr='icontains')
    class Meta:
        models = Berita
        fields = '__all__'
        exclude = ['tanggal','short_line','isi_berita','note','date_added']

class ArtikelFilter(django_filters.FilterSet):
    tipe = CharFilter(field_name = 'tipe', lookup_expr='icontains')
    class Meta:
        models = Artikel
        fields = '__all__'
        exclude = ['judul_artikel','short_line','isi_artikel','author']

class ContactFilter(django_filters.FilterSet):
    nama = CharFilter(field_name = 'nama', lookup_expr='icontains')
    class Meta:
        models = Contact
        fields = '__all__'
        exclude = ['jenis_contact','nama_jenis','nomor_hp']