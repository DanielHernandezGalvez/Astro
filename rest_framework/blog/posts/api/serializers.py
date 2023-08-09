from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'create_at'] # devuelve lo que se solicitó
        # fields = '__all__' devuelve todo