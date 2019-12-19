from rest_framework import serializers

from apps.core.models import Table, Order


class TableSerializer(serializers.ModelSerializer):

    reserved = serializers.SerializerMethodField()

    class Meta:
        model = Table
        fields = (
            'pk', 'number', 'seats', 'shape', 'position_x', 'position_y',
            'length', 'width', 'reserved'
        )

    def get_reserved(self, table: Table):
        date = self.context['date']
        return table.orders.filter(date=date).exists()


class OrderSerializer(serializers.ModelSerializer):

    table = serializers.SlugRelatedField(
        queryset=Table.objects.all(),
        slug_field='number'
    )

    class Meta:
        model = Order
        fields = ('pk', 'table', 'email', 'date')

    def validate(self, attrs):
        if not self.instance:
            table = attrs['table']
            date = attrs['date']
            if Order.objects.filter(table=table, date=date).exists():
                raise serializers.ValidationError(
                    'Table is unavailable at this date. '
                    'Select another one, please.'
                )
        return attrs
