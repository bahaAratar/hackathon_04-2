from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from .models import Project , Category
from .serializers import ProjectSerializer, CategorySerializer

class ProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['client'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)






class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = Project.objects.filter(is_active=True, is_completed=False)
        return qs

    def post(self, request, *args, **kwargs):
        project_id = request.data.get('project_id')
        if not project_id:
            return Response({'error': 'project_id is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        project = Project.objects.filter(id=project_id, is_active=True, is_completed=False).first()
        if not project:
            return Response({'error': 'Invalid project_id.'}, status=status.HTTP_404_NOT_FOUND)

        project.is_active = False
        project.save()
        serializer = self.get_serializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)



class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]