from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view 
from .models import Post 
from .serializers import PostSerializer



@api_view(http_method_names=['GET', 'POST'])
def home(request:Request):
    if request.method == 'POST':
        data = request.data
        response={"message":"hello there",
                  "data":data,
                  }
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {"message":"Hello world"}
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def list_posts(request:Request):
    posts = Post.objects.all()
    serializer = PostSerializer(instance=posts, many=True)
    response = {
        "message":"posts",
        "data":serializer.data
    }
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def single_post(request: Request, post_id :int):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(instance=post)
    
    if post:
        response = {
            "message":"single post",
            "data":serializer.data
        }
        
        return Response(data=response, status=status.HTTP_200_OK)
    return Response(data={"error":"Post not found"}, status=status.HTTP_404_NOT_FOUND)