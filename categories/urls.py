from django.urls import path
from categories import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="categories.index"),
    path('<int:category_id>', views.show, name="categories.show"),
    path('all/', views.all_categories, name="categories.all"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



