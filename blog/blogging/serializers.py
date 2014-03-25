from rest_framework import serializers

from blogging.models import Post, Author

class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')

    def get_id(self, obj):
        return obj.id

    class Meta:
        model = Author
        #read_only_fields = ('email',)
        #fields = ('id', 'name', 'email',)

class PostSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')

    def get_id(self, obj):
        return obj.id

    class Meta:
        model = Post
