from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
import datetime

from .serializers import MemberSerializer
from .models import Member


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('name')
    serializer_class = MemberSerializer









