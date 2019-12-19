from django.utils import timezone
from rest_framework import mixins, viewsets

from apps.core.models import Table, Order
from .serializers import TableSerializer, OrderSerializer


class TableViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = TableSerializer
    queryset = Table.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['date'] = self.request.GET.get('date', timezone.now())
        return context


class OrderViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
