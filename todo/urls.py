from django.urls import path
from .views import Index, CreateTodoView


urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('create/', CreateTodoView.as_view(), name="create")
]