from rest_framework.test import APITestCase
from apps.products.models import Product
from apps.boxes.models import Box
from apps.boxes.services import recommend_box
from apps.orders.models import Order

# test box recommendation for orders
class OrderRecommendationTest(APITestCase):

    # Create test products and boxes 
    def setUp(self):
        self.product = Product.objects.create(name="Mobile", length=10, width=5, height=2, weight=0.5)
        self.small_box = Box.objects.create(name="Small Box", length=15, width=15, height=15, max_weight=5, cost=20)
        self.large_box = Box.objects.create(name="Large Box", length=40, width=40, height=40, max_weight=20, cost=70)

    # test the cheapest suitable box is recommended
    def test_order_recommends_cheapest_suitable_box(self):
        response = self.client.post("/api/orders/", {
            "items": [{"product": self.product.id, "quantity": 1}]
        }, format="json")

        order = Order.objects.get(id=response.data["id"])
        recommended_box = recommend_box(order)

        self.assertEqual(recommended_box.name, "Small Box")

    # tests  None is returned when no suitable box exists
    def test_no_suitable_box(self):
        heavy_product = Product.objects.create(name="Heavy Product", length=10, width=10, height=10, weight=25)

        response = self.client.post("/api/orders/", {
            "items": [{"product": heavy_product.id, "quantity": 1}]
        }, format="json")

        order = Order.objects.get(id=response.data["id"])
        recommended_box = recommend_box(order)

        self.assertIsNone(recommended_box)