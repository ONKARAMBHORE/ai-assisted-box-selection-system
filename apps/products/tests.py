from rest_framework.test import APITestCase
from rest_framework import status

# test cases for the product
class ProductAPITest(APITestCase):

    # test valid product creations
    def test_create_product(self):
        data = {"name": "Mobile", "length": "10", "width": "5", "height": "2", "weight": "0.500"}
        response = self.client.post("/api/products/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # test invalid products dimension
    def test_invalid_product_dimensions(self):
        data = {"name": "Invalid Product", "length": "-10", "width": "5", "height": "2", "weight": "0.500"}
        response = self.client.post("/api/products/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)