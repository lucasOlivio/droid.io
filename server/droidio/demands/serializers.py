from django.utils import timezone

from rest_framework import serializers

from .models import Demand


class DemandSerializer(serializers.ModelSerializer):
    """ Serializer to create, list, update and delete demands
    """

    user_created = serializers.StringRelatedField()

    class Meta:
        model = Demand
        fields = "__all__"
        read_only_fields = (
            "user_created",
            "date_created",
            "user_updated",
            "date_updated",
            "date_completed",
        )

    def update(self, instance, valid_data):
        # Set default user updated for current user and updated date
        instance.user_updated = self.context["request"].user
        instance.date_updated = timezone.now()
        # If demand is completed set completed date
        if valid_data.get("is_completed", False) and not instance.is_completed:
            instance.date_completed = timezone.now()
        elif "is_completed" in valid_data and not valid_data.get("is_completed", False):
            instance.date_completed = None
        return super().update(instance, valid_data)

    def create(self, valid_data):
        # Set default user created for current user
        valid_data["user_created"] = self.context["request"].user
        return Demand.objects.create(**valid_data)
