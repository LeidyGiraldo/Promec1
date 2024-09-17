from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import mantenimiento_view
from .views import notifications_view
from .views import categorias_view

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('modulacion/', views.Ad_servicios, name='modulacion'),
    path('contacto/', views.Contacto, name='contacto'),
    path('inventario/', views.Inventario, name='inventario'),
    path('login/', views.Login_view, name='login'),
    path('register/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='salir'),
    path('produccion/', views.Produccion, name='produccion'),
    path('citas/', views.Citas, name='citas'),
    path('eliminar-cita/<int:id>/', views.eliminar_cita, name='eliminar_cita'),
    path('solicitar-cita/', views.Solicitar_cita, name='cita'),
    path('crear-producto-inv/', views.Crear_inventario, name='crear_product_inv'),
    path('editar-producto/<int:id>/', views.Editar_producto, name='editar_producto'),
    path('eliminar-producto/<int:id>/', views.Eliminar_producto, name='eliminar_producto'),
    path('crear-produccion/', views.Crear_produccion, name='crear_produccion'),
    path('editar_produccion/<int:id>/', views.Editar_produccion, name='editar_produccion'),
    path('eliminar-produccion/<int:id>/', views.Eliminar_produccion, name='eliminar_produccion'),
    path('calificacion/<int:id>/', views.Calificacion_view, name='calificacion' ),
    path('reporte-excel-inventario/', views.Generar_excel_inventario, name='reporte_inventario'),
    path('reporte-excel-produccion/', views.General_excel_produccion, name='reporte_produccion'),
    path('reporte-excel-citas/', views.General_excel_citas, name='reporte_citas'),
    path('clientes/', views.ClientesView.as_view(), name='clientes'),
    path('calendario/', views.calendario_view, name='calendario'),
    path('mantenimiento/', mantenimiento_view, name='mantenimiento'),
    path('notifications/', notifications_view, name='notifications'),
    path('pedidos/', views.pedidos_view, name='pedidos'),
    path('productos/', views.productos_list, name='productos_list'),
    path('categorias/', categorias_view, name='categorias'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)