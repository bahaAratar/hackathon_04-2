from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Category, Project
from .serializers import CategorySerializer, ProjectSerializer
from rest_framework.viewsets import ModelViewSet


class CategoryModelViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProjectModelViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
