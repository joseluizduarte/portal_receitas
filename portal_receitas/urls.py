"""portal_receitas URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from receitas import urls as receitas_url


urlpatterns = [
    path('', include(receitas_url)),
    path('admin/', admin.site.urls),
]
