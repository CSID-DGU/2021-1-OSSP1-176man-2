from django.contrib import admin
from django.urls import path
from apps.main_app import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('trans/', views.trans, name='trans'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
