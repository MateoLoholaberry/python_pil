# Django imports
from django.urls import path

# views imports
from contactoApp.views import ListaContactosApiView, AgregarContactoApiView, ModificarContactoApiView


urlpatterns = [
    path('lista-contactos/', ListaContactosApiView.as_view(), name='contact_list'),
    path('agregar-contacto/', AgregarContactoApiView.as_view(), name='add_contact'),
    path('modificar-contacto/<int:pk>/', ModificarContactoApiView.as_view(), name='modify_contact')
]
