# config/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('', include('pages.urls')),
    path('api/', include('api.urls')),
    path('daytrack/', include('daytrack.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
