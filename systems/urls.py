from django.urls import path
from systems.views import system_list, system_card


urlpatterns = [
    path('', system_list, name='systems-system_list'),
    path('', system_card, name='systems-system_card'),
]
