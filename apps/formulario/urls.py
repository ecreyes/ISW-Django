from django.conf.urls import include, url
from apps.formulario.views import form_file
app_name = 'apps'
urlpatterns = [
    url('',form_file,name='formulario_archivo'),
]
