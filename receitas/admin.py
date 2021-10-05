from django.contrib import admin

from receitas.models import Tag, Produto, Ingrediente, Receita

admin.site.register(Tag)
admin.site.register(Produto)
admin.site.register(Ingrediente)
admin.site.register(Receita)