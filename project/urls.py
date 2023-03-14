from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import CategoryListView, ProjectCreateView, ProjectDetailView, ProjectListView



urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('categories/<int:category_id>/subcategories/', SubCategoryListView.as_view(), name='subcategory-list'),
    path('projects/', ProjectListView.as_view(), name='proj')

]