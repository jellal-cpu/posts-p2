from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser 
from posts.models import Posts 
from posts.serializers import PostSerializer 
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated 


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt 
def posts_list(request):
    """
    List all code posts, or create a new post.
    """
    if request.method == 'GET':
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def post_detail(request, pk):
    """
    Retrieve, update or delete a post.
    """
    try:
        post = Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)



