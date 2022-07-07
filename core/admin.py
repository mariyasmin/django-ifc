from django.contrib import admin

from core.models import Autor, Editora, Categoria, Livro

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)