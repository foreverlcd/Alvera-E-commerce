from .models import Category

# Esto lo agregamos en settings.py para que se ejecute el context processor
# Context processor para añadir los enlaces de la barra de navegación
def menu_links(request):
    links = Category.objects.all()
    # Retornar un diccionario con el nombre de la variable de contexto y su valor
    return dict(links=links)
