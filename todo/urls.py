from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/<int:pk>/', views.todo_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)