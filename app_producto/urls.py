from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.listar_producto, name='listar_producto'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),
]