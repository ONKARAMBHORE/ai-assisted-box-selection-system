from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.boxes.services import recommend_box
from .models import Order
from .serializers import OrderSerializer


# Order logic viewset
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related("items__product").order_by("-created_at")
    serializer_class = OrderSerializer
    http_method_names = ["get", "post", "delete"]

    # Returns the recommended box for a specific order
    @action(detail=True, methods=["get"], url_path="recommend-box")
    def recommend_box(self, request, pk=None):
        order = self.get_object()
        box = recommend_box(order)

        if not box:
            return Response({
                "order_id": order.id,
                "recommended_box": None,
                "message": "No suitable box found."
            }, status=status.HTTP_200_OK)

        return Response({
            "order_id": order.id,
            "recommended_box": {
                "id": box.id,
                "name": box.name,
                "cost": box.cost
            }
        })