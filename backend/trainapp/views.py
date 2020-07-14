from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from trainapp.serializers import UserSerializer
from rest_framework import viewsets
# Create your views here.


def index(request):
    return HttpResponse("<h1>This is first</h1>")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serialize_class = UserSerializer
