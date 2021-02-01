from django.contrib import admin
from .models import Demand


@admin.register(Demand)
class DemandAdmin():
    pass
