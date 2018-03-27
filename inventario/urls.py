from django.conf.urls import include, url
from .import views
from django.urls import path

app_name = 'inventario'

urlpatterns = [
    path('',  views.compania_list),
    path('<int:compania_id>/', views.compania_detail, name='compania_detail'),
    

]