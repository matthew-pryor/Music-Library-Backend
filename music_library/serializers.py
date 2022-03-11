from rest_framework import serializers
from .models import Music
from django.db.models import Count, Sum, Value
from django.db.models.functions import Coalesce

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'genre']