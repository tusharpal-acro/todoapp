from django.http import HttpResponse
from .models import Category, Todo
from .serializers import CategorySerializer, TodoSerializer
from rest_framework import generics
from django.core import serializers as ser
from django.core.cache import cache

# Create your views here.
def index(request):
    return HttpResponse("Todo API App  with Nested Categories")

class ListCategories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RetrieveCategory(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class UpdateCategory(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class DeleteCategory(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class RetrieveTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'

class UpdateTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'

class DeleteTodo(generics.RetrieveDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'


def all_in_category(request, category_name):
    queryset = Todo.objects.filter(category__name=category_name)
    qs_json = ser.serialize('json', queryset)
    return HttpResponse(qs_json, content_type='application/json')

