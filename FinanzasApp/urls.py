
from django.urls import path

from .views import *

urlpatterns = [
    path('', homeFinanzas, name='home'),

    path('personas/', PersonaList.as_view(), name="personas"),
    path('persona_create/', PersonaCreate.as_view(), name="persona_create"),
    path('persona_update/<int:pk>/', PersonaUpdate.as_view(), name="persona_update" ),
    path('persona_delete/<int:pk>/', PersonaDelete.as_view(), name="persona_delete" ),

    path('formas_de_pago/', FormaDePagoList.as_view(), name="formas_de_pago"),
    path('formas_de_pago_create/', FormaDePagoCreate.as_view(), name="formas_de_pago_create"),
    path('formas_de_pago_update/<int:pk>/', FormaDePagoUpdate.as_view(), name="formas_de_pago_update" ),
    path('formas_de_pago_delete/<int:pk>/', FormaDePagoDelete.as_view(), name="formas_de_pago_delete" ),

    path('ingresos/', IngresoList.as_view(), name="ingresos"),
    path('ingresos_create/', IngresoCreate.as_view(), name="ingresos_create"),
    path('ingresos_update/<int:pk>/', IngresoUpdate.as_view(), name="ingresos_update" ),
    path('ingresos_delete/<int:pk>/', IngresoDelete.as_view(), name="ingresos_delete" ),

    path('egresos/', EgresoList.as_view(), name="egresos"),
    path('egresos_create/', EgresoCreate.as_view(), name="egresos_create"),
    path('egresos_update/<int:pk>/', EgresoUpdate.as_view(), name="egresos_update" ),
    path('egresos_delete/<int:pk>/', EgresoDelete.as_view(), name="egresos_delete" ),

    path('ingresos_buscar/', encontrarIngresosPorTitular, name="ingresos_buscar" ),
    path('egresos_buscar/', encontrarEgresosPorTitular, name="egresos_buscar" ),
]
