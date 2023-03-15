from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import viewsets , generics
from .serializers import *
from .models import *
# from rest_framework import viewsets
# from rest_framework import generics
# from .models import Category, Project
# from .serializers import CategorySerializer, ProjectSerializer
# from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectDetailSerializer
    queryset = Project.objects.all()
    lookup_url_kwarg = 'project_id'