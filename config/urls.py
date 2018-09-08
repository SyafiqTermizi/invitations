from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('dashboards.urls')),
    path('invite/', include('invitations.urls')),
    path('admin/', admin.site.urls),
]
