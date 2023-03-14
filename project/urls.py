from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewset, ProjectCreateAPIView, ProjectListAPIView

router = DefaultRouter()
router.register('category', CategoryModelViewset)


urlpatterns = [
    path('get/', ProjectListAPIView.as_view()),
    path('create/', ProjectCreateAPIView.as_view()),
    path('project', include(router.urls)),


]