from django.shortcuts import render
from rest_framework import generics

from .models import Users
from .serialisers import UsersSerializer
# Create your views here.

class UsersAPI(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer