from django.urls import path
from apps.trayectoria.views import index
from django.contrib.auth.decorators import login_required

app_name = 'apps'
urlpatterns = [
    path('', login_required(index),name='trayectoria_index'),
]