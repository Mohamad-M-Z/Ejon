from rest_framework import serializers
from ...models import Blog


# class PostSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)



class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "Author", "category", "content", "status", "created_date", "published_date"]
