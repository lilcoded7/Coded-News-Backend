from rest_framework import serializers
from news.models import BlogNew


class BlogNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogNew
        fields = '__all__'