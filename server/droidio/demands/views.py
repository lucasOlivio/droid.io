from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Demand
from .permissions import IsOwnerOrAdmin
from .serializers import DemandSerializer


class DemandViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """ Updates, deletes and retrieves demands
    """

    serializer_class = DemandSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Demand.objects.filter(user_created=self.request.user)
        return Demand.objects.all()
