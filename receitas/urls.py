"""receitas URL Configuration"""

# Componentes do Django
from django.urls import path, include
# Componentes próprios
from receitas.views import HomePageView, ReceitaView, TagPageView, BuscaPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('receita/<int:pk>', ReceitaView.as_view(), name='receita'),
    path('tag/<str:tag>', TagPageView.as_view(), name='tag'),
    path('busca', BuscaPageView.as_view(), name='busca'),
]
