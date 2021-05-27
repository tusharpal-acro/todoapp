from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home-page"),
    path('create-category/', views.CreateCategory.as_view(), name="create-category"),
    path('categories/', views.ListCategories.as_view(), name="categories"),
    path('retrieve-category/<id>/', views.RetrieveCategory.as_view(), name="retrieve-category"),
    path('update-category/<id>/', views.UpdateCategory.as_view(), name="update-category"),
    path('delete-category/<id>/', views.DeleteCategory.as_view(), name="delete-category"),

    path('create-todo/', views.CreateTodo.as_view(), name="create-todo"),
    path('todos/', views.ListTodo.as_view(), name="todos"),
    path('retrieve-todo/<id>/', views.RetrieveTodo.as_view(), name="retrieve-todo"),
    path('update-todo/<id>/', views.UpdateTodo.as_view(), name="update-todo"),
    path('delete-todo/<id>/', views.DeleteTodo.as_view(), name="delete-todo"),
    path('taskbycategory/<category_name>', views.all_in_category, name="all_in_category"),

]
