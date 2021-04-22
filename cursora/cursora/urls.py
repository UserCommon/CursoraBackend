from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .views import MainApiView

urlpatterns = [
    path('', MainApiView.as_view()),
    path('apiv1/admin/', admin.site.urls),
    path('apiv1/', include('main.urls')),
    path('apiv1/', include('accounts.urls')),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
