from django.shortcuts import render
from Blog.models import Post
from .serializers import PostSerialiizers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET",])
def api_homepage(request):
    all_posts = Post.objects.all() #returns the queryset
    new_serialized_data = PostSerialiizers(all_posts, many=True)
    return Response(new_serialized_data.data)

@api_view(["GET"])
def api_detailedpage(request,id):
    single_post = Post.objects.get(id=id)
    serialized_post = PostSerialiizers(single_post)
    return Response(serialized_post.data)


@api_view(["PUT"])
def api_updatepage(request, id):
    single_post = Post.objects.get(id=id)
    new_data = request.data
    serialized_new_data = PostSerialiizers(single_post, data=new_data, partial=True)
    if serialized_new_data.is_valid():
        serialized_new_data.save()
        return Response(serialized_new_data.data)
    else:
        return Response({"Error": "You typed rubbish!!"})



@api_view(["DELETE"])
def api_deletepage(request, id):
    single_post = Post.objects.get(id=id)
    single_post.delete()
    return Response({"success": "Your post has been deleted"})


@api_view(["POST"])
def api_createpage(request):
    new_data = PostSerialiizers(data=request.data)
    if new_data.is_valid():
        new_data.save()
        return Response(new_data.data)
