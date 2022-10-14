from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_view, name='home'),
    path('ports', views.get_ports_view, name='ports'),
    path('add_port', views.add_port_view, name='add_port_view'),
    path('add_port_page', views.add_port_page, name='add_port_page'),
    path('edit_port/<int:id>', views.edit_port, name='edit_port'),
    path('del_port/<int:id>', views.del_port, name='del_port'),
    path('upload_csv_page',views.upload_csv_page,name='upload_csv_page'),
    path('trips', views.get_trips_view, name='trips'),
    path('add_trip', views.add_trip_view, name='add_trip_view'),
    path('add_trip_page', views.add_trip_page, name='add_trip_page'),
    path('edit_trip/<int:id>', views.edit_trip, name='edit_trip'),
    path('del_trip/<int:id>', views.del_trip, name='del_trip'),
    path('plots', views.get_plot_view, name='plots'),

]