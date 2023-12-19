
from django.contrib import admin
from django.urls import path
from appfrontend.views import home, create_task, manage_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('create/', create_task, name='create'),
    path('manage/<int:task_id>', manage_task, name='manage'),
]
