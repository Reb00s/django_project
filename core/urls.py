from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('dashboard.urls')),
    path('system/', include('systems.urls')),
    path('admin/', admin.site.urls),
]
