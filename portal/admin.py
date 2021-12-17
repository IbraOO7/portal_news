from django.contrib import admin
from .models import *

class PostingAdmin(admin.ModelAdmin):
    list_display = ('id','judul','status','waktu_publish','kategori','konten','author')
    list_display_links = ('id','judul')
    search_fields = ('judul',)
    list_per_page = 25

admin.site.register(Posting, PostingAdmin)
admin.site.register(Komentar)
admin.site.register(Kategori)

