from datetime import datetime

from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from .models import Category,Todo
from .serializers import CategorySerializer, TodoSerializer
from django.urls import reverse
from rest_framework.views import status

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()
    @staticmethod
    def create_category(name=""):
        if name != "":
            Category.objects.create(name=name)

    def setUp(self):
        self.create_category("Studying")
        self.create_category("Household Work")
        self.create_category("Office Work")

    @staticmethod
    def create_todo(title="", description = "", assigned_date = "", category=""):
        if title != "":
            Todo.objects.create(title=title, description =description, assigned_date =assigned_date, category=category)

    def setUp(self):
        try:
            category = Category.objects.get(name = 'Studying')
        except:
            category=Category.objects.create(name='Studying')

        self.create_todo("Learn R", "Complete it by weekend", '2021-09-09', category)
        # self.create_category("Household Work")
        # self.create_category("Office Work")



class GetAllCategories(BaseViewTest):

    def test_get_all_categories(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("categories")
        )
        # fetch the data from db
        expected = Category.objects.all()
        serialized = CategorySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetAllTodo(BaseViewTest):

    def test_get_all_todo(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("todos")
        )
        # fetch the data from db
        expected = Todo.objects.all()
        serialized = TodoSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
