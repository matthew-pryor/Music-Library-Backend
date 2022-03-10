from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import MusicSerializer
from .models import Music


# Create your views here.

@api_view(['GET', 'POST'])
def music_library_list(request):
    
    if request.method == 'GET':

        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':

        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def music_library_detail(request, pk):
    pass