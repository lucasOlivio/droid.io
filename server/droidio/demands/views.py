from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Demand
from .permissions import IsOwnerOrAdmin
from .serializers import DemandSerializer
from .mixins import DemandsListMixin


class DemandViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates, deletes and retrieves demands
    """
    serializer_class = DemandSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin,)

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Demand.objects.filter(
                user_created=self.request.user
            )
        return Demand.objects.all()


class DemandCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates demands
    """
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer
    permission_classes = (IsAuthenticated,)
