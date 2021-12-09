from rest_framework import serializers
from tagsApp.models import ReadTagsOrder, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['strEPC', 'antenna', 'strRSSI', 'nReadCount', 'readtagorder']

class ReadTagsOrderSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    
    class Meta:
        model = ReadTagsOrder
        fields = ['scan_time']