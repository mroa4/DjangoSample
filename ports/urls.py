from django.urls import path
from . import views

urlpatterns = [
    path('', views.ports_view, name='ports'),
    path('add_port', views.add_port_view, name='add_port_view'),
    path('add_port_page', views.add_port_page, name='add_port_page'),
]