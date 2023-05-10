from rest_framework import serializers
from Blog.models import Post


class PostSerialiizers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        fields = ["title", "content", "author", "date_posted"]