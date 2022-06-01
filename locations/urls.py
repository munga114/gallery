from django.urls import path
from locations import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="locations.index"),
    path('<int:location_id>', views.show, name="locations.show"),
    path('all', views.get_all_locations, name="locations.all")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)