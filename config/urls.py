# config/urls.py
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('', include('pages.urls')),
    path('api/', include('api.urls')),
    path('daytrack/', include('daytrack.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
