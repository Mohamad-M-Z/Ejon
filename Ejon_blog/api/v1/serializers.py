from rest_framework import serializers
from ...models import Blog, Category
from django.contrib.auth.models import User 


# class PostSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]



class PostSerializers(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relativ_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    # category = CategorySerializers()
    # category = serializers.SlugRelatedField(many=False, slug_field='name',queryset=Category.objects.all())

    class Meta:
        model = Blog
        fields = ["id", "title", "image", "Author", "category", "snippet", "relativ_url" ,"absolute_url" ,"content", "status", "created_date", "published_date"]
        read_only_fields = ['author']

    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)

        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('relativ_url', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)

        rep['category'] = CategorySerializers(instance.category).data
        return rep
    

    def create(self, validated_data):
        validated_data['author']  = User.objects.get(user__id =  self.context.get('request').user.id) 
        return super().create(validated_data)


