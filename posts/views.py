from django.shortcuts import render
from rest_framework import generics
from . import models, serializers

#this views all DB
class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

#this command Creates new Data
class PostCreateSerializer(generics.CreateAPIView):
    query = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

#this command generates Update and Delete
class PostUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
