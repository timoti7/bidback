# mmd/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from product.views import CSRFTokenView  # CSRFTokenView'ı içe aktarın

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('product.urls')),  # product uygulamasının URL'lerini dahil edin
    path('common/', include('common.urls')),
    path('get-csrf-token/', CSRFTokenView.as_view(), name='get-csrf-token'),  # CSRFTokenView için URL yolu
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
