from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from nose.tools import eq_
from faker import Faker
import factory
import json

from ..models import Demand
from .factories import DemandFactory
from ..serializers import DemandSerializer

from droidio.users.models import User
from droidio.users.test.factories import UserFactory

fake = Faker()


class TestDemandListTestCase(APITestCase):
    """ Tests /demands list operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.url = reverse("demands-list")
        self.demand_data = factory.build(dict, FACTORY_CLASS=DemandFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.demand_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        demand = Demand.objects.get(pk=response.data.get("id"))
        eq_(demand.description, self.demand_data.get("description"))

    def test_get_list_returns_only_my_demands(self):
        # Set testing demands
        DemandFactory(user_created=self.user)
        user2 = UserFactory()
        DemandFactory(user_created=user2)
        # Test response and results
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

        demands = Demand.objects.filter(user_created=self.user)
        serializer = DemandSerializer(demands, many=True)
        eq_(response.data["count"], 1)
        eq_(response.data["results"], serializer.data)


class TestDemandDetailTestCase(APITestCase):
    """ Tests /demands detail operations.
    """

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.demand = DemandFactory(user_created=self.user)
        self.url = reverse("demands-detail", kwargs={"pk": self.demand.pk})

    def test_get_request_returns_a_given_demand(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_patch_request_updates_a_demand(self):
        new_description = fake.text()
        payload = {"description": new_description}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        demand = Demand.objects.get(pk=self.demand.id)
        eq_(demand.description, new_description)

    def test_put_request_updates_a_demand(self):
        payload = factory.build(dict, FACTORY_CLASS=DemandFactory)
        response = self.client.put(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        demand = Demand.objects.get(pk=self.demand.id)
        eq_(demand.description, payload["description"])

    def test_delete_request_deletes_a_demand(self):
        response = self.client.delete(self.url)
        eq_(response.status_code, status.HTTP_204_NO_CONTENT)

        demand = Demand.objects.filter(pk=self.demand.id).first()
        eq_(demand, None)
