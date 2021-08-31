from django.urls import path
from .views import ListTodoView, CreateTodoView, test_view

urlpatterns = [
    path('', ListTodoView.as_view()),
    path('create/', CreateTodoView.as_view()),
    path('test/', test_view)
]
