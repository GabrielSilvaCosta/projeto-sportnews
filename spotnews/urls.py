
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from news.views import CategoryListAPIView, UserListAPIView, NewsListAPIView


router = DefaultRouter()

router.register(r'categories', CategoryListAPIView)
router.register(r'users', UserListAPIView)
router.register(r'news', NewsListAPIView)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("news.urls")),
    path("api/", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
