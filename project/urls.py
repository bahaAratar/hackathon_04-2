from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='category')
router.register('projects', ProjectViewSet, basename='project')
# router.register('orders', OrderViewSet, basename='order')
# router.register('ratings', RatingViewSet, basename='rating')

urlpatterns = [
    path('projects/<int:project_id>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('projects/<int:project_id>/apply/', AddCandidateAPIView.as_view(), name='project-apply'),
    path('projects/<int:project_id>/choose_executor/', ChooseExecutorAPIView.as_view(), name='choose_executor'),
    path('', include(router.urls)),
   
]