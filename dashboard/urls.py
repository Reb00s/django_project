from django.urls import path
from dashboard.views import start_page


urlpatterns = [
    path('', start_page, name='dashboard-start_page'),
]
