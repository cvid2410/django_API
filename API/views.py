from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import PostSerializer
from .models import Post

from rest_framework import generics, mixins

class PostView( mixins.CreateModelMixin ,mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    




        
        

# class TestView(APIView):

#     permission_classes = [IsAuthenticated]


#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# class TestView(APIView):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'name':'carlos',
#             'age': 23,
#         }
#         return Response(data)

# def test_view(request):
#     data = {
#         'name':'carlos',
#         'age': 23,
#     }
#     return JsonResponse(data)
