from django.shortcuts import render
from news.serializers import BlogNewsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, mixins, generics
from news.models import BlogNew

# Create your views here.


class BlogNewViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = BlogNew.objects.all()
    serializer_class = BlogNewsSerializer
    permission_classes = [AllowAny]


class BlogNewsCategory(APIView):
    def get(self, request, category_id):
        blog_news = BlogNew.objects.filter(category_id=category_id)
        data = BlogNewsSerializer(blog_news, many=True).data
        return Response({'data':data})