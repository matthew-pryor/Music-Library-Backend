from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import MusicSerializer
from .models import Music


# Create your views here.

@api_view(['GET'])
def music_library_list(request):
    pass

@api_view(['GET'])
def music_library_detail(request, pk):
    pass