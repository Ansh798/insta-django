from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from insta.models import *
from insta.serializer import *


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class CreateUser(generics.CreateAPIView):
#     queryset=User.objects.all()
#     ser=UserSerializer