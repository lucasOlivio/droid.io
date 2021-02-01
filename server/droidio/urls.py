from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .users.views import UserViewSet, UserCreateViewSet
from .demands.views import DemandViewSet


router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"users", UserCreateViewSet)
router.register(r"demands", DemandViewSet, basename="demands")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
