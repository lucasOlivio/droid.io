from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class CompleteDemandMixin(object):
    """ Set demand as completed and set its completed date """
    @action(detail=True, methods=['post'])
    def set_completed(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if serializer.set_completed(instance):
            return Response(serializer.data)
        else:
            return Response({"error": "This demand has already been completed!"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
