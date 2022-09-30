from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_ports_view, name='ports'),
    path('add_port', views.add_port_view, name='add_port_view'),
    path('add_port_page', views.add_port_page, name='add_port_page'),
    path('edit_port/<int:id>', views.edit_port, name='edit_port'),
    path('del_port/<int:id>', views.del_port, name='del_port'),
    path('upload_csv_page',views.upload_csv_page,name='upload_csv_page'),
]