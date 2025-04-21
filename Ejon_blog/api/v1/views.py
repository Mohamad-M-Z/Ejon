from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers, CategorySerializers
from ...models import Blog, Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins, viewsets

from rest_framework.decorators import action
from .paginations import LargeResultsSetPagination
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


"""
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
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

"""
'''class BlogList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers

    """ getting a lis of blog and creating new blog """
    def get(self, request):
        blog = Blog.objects.filter(status=True)
        serialize = PostSerializers(blog, many=True)
        return Response(serialize.data)

    def post(self, request):
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''


class BlogList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Blog.objects.filter(status=True)



# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def BlogDetail(request, id):
#     blog = get_object_or_404(Blog ,pk=id, status=True)
#     if request.method == "GET":
#         serialize = PostSerializers(blog)
#         return Response(serialize.data)
#     elif request.method == "PUT":
#         serializer = PostSerializers(blog, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         blog.delete()
#         return Response("itme deleted", status=status.HTTP_204_NO_CONTENT)
 
'''
class BlogDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializers_class = PostSerializers

    def get(self,request, id):
        blog = get_object_or_404(Blog ,pk=id, status=True)
        serialize = self.serializers_class(blog)
        return Response(serialize.data)
    
    def put(self, request, id):
        blog = get_object_or_404(Blog ,pk=id, status=True)
        serializer = PostSerializers(blog, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        blog = get_object_or_404(Blog ,pk=id, status=True)
        blog.delete()
        return Response("itme deleted", status=status.HTTP_204_NO_CONTENT)


'''

# class BlogDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializers
#     queryset = Blog.objects.filter(status=True)



class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializers
    queryset = Blog.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_fields = ['category', 'status']
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    pagination_class = LargeResultsSetPagination

    # @action(methods=["get"], detail=False)
    # def get_ok(self, request):
    #     return Response({'detail':'ok'})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

