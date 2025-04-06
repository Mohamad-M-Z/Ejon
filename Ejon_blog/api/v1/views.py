from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers
from ...models import Blog
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"])
def Bloglist(request):
    if request.method == "GET":
        blog = Blog.objects.filter(status=True)
        serialize = PostSerializers(blog, many=True)
        return Response(serialize.data)
    
    elif request.method == "POST":
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



@api_view(["GET", "PUT", "DELETE"])
def BlogDetail(request, id):
    blog = get_object_or_404(Blog ,pk=id, status=True)
    if request.method == "GET":
        serialize = PostSerializers(blog)
        return Response(serialize.data)
    elif request.method == "PUT":
        serializer = PostSerializers(blog, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        blog.delete()
        return Response("itme deleted", status=status.HTTP_204_NO_CONTENT)
 
