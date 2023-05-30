from django.urls import path
from .views import UsersAPI

urlpatterns = [
    path('api/users/', UsersAPI.as_view(), name="api_users")
]
