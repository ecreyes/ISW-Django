from django.urls import path
from apps.trayectoria.views import index

app_name = 'apps'
urlpatterns = [
    path('', index,name='trayectoria_index'),
]
