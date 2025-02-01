from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse, HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
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


class PostListCreateView(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    # def get(self, *args, **kwargs):
    #     posts = Post.objects.all()
    #     serializer = self.serializer_class(instance=posts, many=True)
        
    #     response = {
    #         "message":"Posts",
    #         "data":serializer.data
    #     }
    #     return Response(data=response, status=status.HTTP_200_OK)
    
    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = self.serializer_class(data=data)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         response = {
    #             "message":"Data created successfully, yeahhh",
    #             "data":serializer.data
    #         }
    #         return Response(data=response, status=status.HTTP_201_CREATED)
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveUpdateDeleteView(generics.GenericAPIView,
                                   mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, *kwargs)
    
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    # def get(self, request, post_id:int):
    #     post = get_object_or_404(Post, id=post_id)
    #     serializer = self.serializer_class(instance=post)
        
    #     response = {
    #         "message":"Post",
    #         "data":serializer.data
    #     }
    #     return Response(data=response, status=status.HTTP_200_OK)
    
    # def put(self, request, post_id:int):
    #     post = get_object_or_404(Post, id=post_id)
    #     data = request.data
    #     serializer = self.serializer_class(instance=post, data=data)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         response = {
    #             "message":"Post updated",
    #             "data": serializer.data
    #         }
    #         return Response(data=response, status=status.HTTP_200_OK)
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, post_id:int):
    #     post = get_object_or_404(Post, id=post_id)
    #     post.delete()
        
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(http_method_names=['GET', "POST"])
# def list_posts(request:Request):
#     if request.method == "POST":
#         data = request.data
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message":"Post created successfully",
#                 "data":serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
        
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     posts = Post.objects.all()
#     serializer = PostSerializer(instance=posts, many=True)
#     response = {
#         "message":"posts",
#         "data":serializer.data
#     }
#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=['GET'])
# def single_post(request: Request, post_id :int):
#     post = get_object_or_404(Post, id=post_id)
#     serializer = PostSerializer(instance=post)
    
#     if post:
#         response = {
#             "message":"single post",
#             "data":serializer.data
#         }
        
#         return Response(data=response, status=status.HTTP_200_OK)
    

# @api_view(http_method_names=['DELETE'])
# def delete_post(request:Request, post_id: int):
#     if request.method == "DELETE":
#         post = get_object_or_404(Post, id=post_id)
#         post.delete()
#         response = {
#             "message":"Post deleted successfully",
#         }
            
#         return Response(data=response, status=status.HTTP_404_NOT_FOUND)
        
# @api_view(http_method_names=['PUT'])
# def update_post(request:Request, post_id: int):
#     if request.method == "PUT":
        
#         data = request.data
#         post = get_object_or_404(Post, id=post_id)
        
#         serializer = PostSerializer(instance=post, data=data)
#         if serializer.is_valid():
#             serializer.save()
            
#             response = {
#                 "message":"Post updated successfully",
#                 "data":serializer.data
#             }
            
#             return Response(data=response, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)