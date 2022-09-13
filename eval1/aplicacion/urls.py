from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_pago/', views.form_pago, name="form_pago"),
    path('mostrar_pago/', views.mostrar_pago, name="mostrar_pago"),
    path('salir/', views.salir, name="salir"),
]