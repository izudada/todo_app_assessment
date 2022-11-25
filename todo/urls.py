from django.urls import path
from .views import (
                        Index, CreateTodoView,
                        TodoView, EditTodo,
                        DeleteTodo, CompleteTodo,
                        search
                    )


urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('create/', CreateTodoView.as_view(), name="create"),
    path('create/<int:pk>/', TodoView.as_view(), name="detail"),
    path('<int:pk>/edit/', EditTodo.as_view(), name="edit"),
    path('<int:pk>/delete/', DeleteTodo.as_view(), name="delete"),
    path('<int:pk>/completed/', CompleteTodo.as_view(), name="complete"),
    path('search/', search, name="search"),
]