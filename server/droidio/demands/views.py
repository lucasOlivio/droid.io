from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Demand
from .permissions import IsOwnerOrAdmin
from .serializers import DemandSerializer
from .mixins import CompleteDemandMixin


class DemandViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    CompleteDemandMixin,
    viewsets.GenericViewSet,
):
    """ Updates, deletes and retrieves demands """

    serializer_class = DemandSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Demand.objects.filter(user_created=self.request.user)
        return Demand.objects.all()

    @method_decorator(cache_page(settings.CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
