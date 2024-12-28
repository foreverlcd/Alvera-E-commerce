from django.urls import path
from . import views

# Importar settings y static
urlpatterns = [
    path('', views.store, name='store'),
    ]