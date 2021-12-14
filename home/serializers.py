from rest_framework import serializers

from home.models import Blogpost


class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blogpost
        fields="__all__"