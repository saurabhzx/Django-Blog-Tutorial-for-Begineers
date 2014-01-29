from rest_framework import serializers

from blogging.models import Post, Author

class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    #name = serializers.SerializerMethodField('get_name')
    #email = serializers.SerializerMethodField('get_email')


    def get_id(self, obj):
        return obj.id

    class Meta:
        model = Author
        #read_only_fields = ('email',)
        #fields = ('id', 'name', 'email',)

class PostSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_id')
    #title = serializers.SerializerMethodField('get_title')
    #date = serializers.SerializerMethodField('get_date')
    #body = serializers.SerializerMethodField('get_body')
    #author_id = serializers.SerializerMethodField('get_author_id')

    def get_id(self, obj):
        return obj.id

    #def get_author_id(self, obj):
     #   return obj.author_id

    class Meta:
        model = Post
