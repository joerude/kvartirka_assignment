from mptt.templatetags.mptt_tags import cache_tree_children  # type: ignore
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer


class CreateComment(CreateAPIView):
    serializer_class = CommentSerializer


class CreateBlog(CreateAPIView):
    serializer_class = BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """Using ViewSets to DRY"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentViewSet(viewsets.ModelViewSet):
    def get(self, request):
        comment_tree = Comment.objects.all().get_descendants(include_self=True)
        comment_tree = cache_tree_children(comment_tree)
        serializer = CommentSerializer(comment_tree[0])
        return Response(serializer.data, status=status.HTTP_200_OK)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
