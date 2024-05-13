from django.contrib import admin
from django.urls import path
from todoapp.views import todoapp_view, add_todo_view, delete_todo_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/', todoapp_view),
    path('add_todo_item/', add_todo_view),
    path('delete_todo_item/<int:i>/', delete_todo_view),
]
