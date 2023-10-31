from django.urls import path
from inicio.views import inicio, remeras, zapas, gorras, crear_remera, crear_zapatillas, crear_gorra

urlpatterns = [
    path('',inicio, name='inicio'),
    path('remeras/',remeras, name='remeras'),
    path('zapas/',zapas, name='zapas'),
    path('gorras/',gorras, name='gorras'),
    path('remeras/crear/',crear_remera, name='crear_remera'),
    path('zapas/crear/',crear_zapatillas, name='crear_zapatillas'),
    path('gorras/crear/',crear_gorra, name='crear_gorra'),
]
