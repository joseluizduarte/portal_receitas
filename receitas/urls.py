from django.urls import path, include

from receitas.views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
