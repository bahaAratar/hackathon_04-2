from django.db import models
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from project.models import *
from project.views import  ProjectViewSet



class ReattingListCreateAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    pass
