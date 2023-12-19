from django.contrib import admin
from django.urls import path
from appbackend.views import list_task, manage_task, create_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_task),
    path('create_task/', create_task),
    path('manage_task/<int:task_id>/', manage_task),
    
]
