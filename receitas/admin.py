"""receitas Admin Configuration"""

# Componentes do Django
from django.contrib import admin
# Componentes próprios
from receitas.models import Tag, Produto, Ingrediente, Receita, Comentario

admin.site.register(Tag)
admin.site.register(Produto)
admin.site.register(Ingrediente)
admin.site.register(Receita)
admin.site.register(Comentario)