from django.contrib import admin

from core.models import Autor,Editora, Categoria 

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)