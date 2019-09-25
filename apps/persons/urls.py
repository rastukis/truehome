# Django
from django.urls import path

# Views
from apps.persons.views import (
    add_person, detail_person
)

app_name = 'persons'

urlpatterns = [
    # Agregar Persona
    path('add/', add_person, name='add_person'),

    # Detalle de la persona
    path('detail/<int:pk>/', detail_person, name='detail_person'),
]