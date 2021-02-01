from django.test import TestCase
from django.forms.models import model_to_dict

from .factories import DemandFactory
from ..serializers import DemandSerializer

from nose.tools import eq_, ok_
import pytest

pytestmark = pytest.mark.django_db


class TestCreateDemandSerializer(TestCase):

    def setUp(self):
        self.demand_data = model_to_dict(DemandFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = DemandSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = DemandSerializer(data=self.demand_data)
        ok_(serializer.is_valid())
