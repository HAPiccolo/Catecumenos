from django.urls import path
from .views import home, consultas, registrar, supervisor



urlpatterns = [

path('', home, name='home'),
path('consultas/', consultas, name='consultas'),
path('registrar/', registrar, name='registrar'),
path('administrador/', supervisor, name='administrador'),

# Al cerrar sesion nos envia al home

]