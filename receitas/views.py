"""receitas Views"""

# Componentes do Django
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
# Componentes de outros módulos
from math import ceil
# Componentes próprios
from receitas.models import Receita, Tag, Comentario

class HomePageView(ListView):
    model = Receita
    template_name = "receitas/home.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_list = Tag.objects.all()
        tamanho = len(tag_list)
        metade = ceil(tamanho/2)
        context['tags_col1'] = tag_list[:metade]
        context['tags_col2'] = tag_list[metade:]
        return context


class ReceitaPageView(DetailView):
    model = Receita
    template_name = "receitas/receita.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comentarios = Comentario.objects.filter(receita_comentario=self.get_object())
        context['comentarios'] = comentarios
        return context


class TagPageView(ListView):
    template_name = "receitas/home.html"
    paginate_by = 3

    def get_queryset(self):
        queryset = Receita.objects.filter(tags__pk=self.kwargs['tag'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_list = Tag.objects.all()
        tamanho = len(tag_list)
        metade = ceil(tamanho/2)
        context['tags_col1'] = tag_list[:metade]
        context['tags_col2'] = tag_list[metade:]
        return context


class BuscaPageView(ListView):
    template_name = "receitas/home.html"
    paginate_by = 3

    def get_queryset(self):
        queryset = Receita.objects.filter(nome__icontains=self.request.GET.get('busca'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_list = Tag.objects.all()
        tamanho = len(tag_list)
        metade = ceil(tamanho/2)
        context['tags_col1'] = tag_list[:metade]
        context['tags_col2'] = tag_list[metade:]
        return context


class ComentarioView(View):
    pass