from rest_framework.test import APITestCase
from rest_framework import status

# test case f box
class BoxAPITest(APITestCase):

    # Test valid box creation
    def test_create_box(self):
        data = {"name": "Small Box", "length": "15", "width": "15", "height": "15", "max_weight": "5", "cost": "20"}
        response = self.client.post("/api/boxes/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)