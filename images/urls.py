from django.urls import path
from images import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('search/', views.search, name="images.search")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)