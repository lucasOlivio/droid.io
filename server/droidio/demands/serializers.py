from django.utils import timezone

from rest_framework import serializers

from .models import Demand


class DemandSerializer(serializers.ModelSerializer):
    """
    Serializer to list, update and delete demands
    """

    class Meta:
        model = Demand
        fields = ('id', 'description', 'is_completed', 'delivery_state',
                    'delivery_city', 'delivery_street', 'delivery_number',
                    'delivery_complement', 'delivery_cep', 'delivery_name',
                    'cellphone', 'email', 'user_created', 'date_created',
                    'user_updated', 'date_updated', 'date_completed')
        read_only_fields = ('user_created', 'date_created', 'user_updated',
                            'date_updated', 'date_completed')

    def update(self, valid_data):
        # Set default user updated for current user and updated date
        valid_data['user_updated'] = self.context['request'].user
        valid_data['date_updated'] = timezone.now
        # If demand is completed set completed date
        if valid_data['is_completed'] and  not valid_data['date_completed']:
            valid_data['date_completed'] = timezone.now
        return Demand.objects.create(**valid_data)
    
    def create(self, valid_data):
        # Set default user created for current user
        valid_data['user_created'] = self.context['request'].user
        return Demand.objects.create(**valid_data)