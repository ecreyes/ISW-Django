from django.urls import path
from apps.usuario.views import RegistroUsuario
app_name = 'apps'
urlpatterns = [
   path('registrar', RegistroUsuario.as_view(),name='registrar'),
]
