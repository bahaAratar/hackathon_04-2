from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Category, Project
from .permissions import IsClient
from .serializers import CategorySerializer, ProjectSerializer, ProjectDetailSerializer, ProjectListSerializer




# class ProjectCreateAPIView(generics.CreateAPIView):
#     serializer_class = ProjectSerializer
#     permission_classes = (IsAuthenticated,)

#     def create(self, request, *args, **kwargs):
#         data = request.data.copy()
#         data['client'] = request.user.id
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)






# class ProjectListAPIView(generics.ListAPIView):
#     serializer_class = ProjectSerializer
#     permission_classes = (IsAuthenticated,)
    
#     def get_queryset(self):
#         qs = Project.objects.filter(is_active=True, is_completed=False)
#         client = self.objects.User
#         qs = qs.data['client']
#         return qs

#     def post(self, request, *args, **kwargs):
#         project_id = request.data.get('project_id')
#         if not project_id:
#             return Response({'error': 'project_id is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
#         project = Project.objects.filter(id=project_id, is_active=True, is_completed=False).first()
#         if not project:
#             return Response({'error': 'Invalid project_id.'}, status=status.HTTP_404_NOT_FOUND)

#         project.is_active = False
#         project.save()
#         serializer = self.get_serializer(project)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
  



# class CategoryModelViewset(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]







class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsClient)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.filter(is_available=True)
    serializer_class = ProjectListSerializer
