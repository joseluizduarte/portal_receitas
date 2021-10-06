from django.shortcuts import render
from django.views.generic import ListView

from receitas.models import Receita

class HomePageView(ListView):
    model = Receita
    template_name = "receitas/home.html"
    paginate_by = 3
