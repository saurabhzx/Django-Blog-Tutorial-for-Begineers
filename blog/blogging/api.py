from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from blogging.serializers import AuthorSerializer,PostSerializer
from blogging.models import Author,Post
from blogging.permissions import *


class AuthorList(generics.ListCreateAPIView):
    model = Author
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AdminOnly,)

class AuthorDetail(generics.RetrieveAPIView):
    model = Author
    serializer_class = AuthorSerializer

    permission_classes = (AdminOnly,)
    lookup_field="id"

    def get_object(self):
        id = self.kwargs.get('id', None)
        return Author.objects.get(id=id)

    def post(self, request, *args, **kwargs):
        self.serializer_class = AuthorSerializer
        author = self.get_object()
        data = request.DATA
        serializer = AuthorSerializer(author, data=data)
        print serializer.data
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

class AuthorPost(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializer
    lookup_field = 'id'
    permission_classes = (AdminOnly,)

    def get_queryset(self):
        queryset = super(AuthorPost,self).get_queryset()
        return queryset.filter(author__pk=self.kwargs.get('id'))

    def post(self, request, *args, **kwargs):
        self.serializer_class = PostSerializer
        post = self.get_object()
        data = request.DATA
        serializer = PostSerializer(post, data=data)
        print serializer.data
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)



class PostList(generics.ListCreateAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = (AdminOnly,)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = (AdminOnly,)
