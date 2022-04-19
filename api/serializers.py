from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework import serializers

from test_django import settings

from .models import Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField('get_comments')

    def get_comments(self, blog):
        """Получение всех комментариев к статье вплоть до 3 (TREE_DEPTH=3) уровня вложенности"""
        _comments = cache_tree_children(Comment.objects.filter(blog=blog,
                                                               level__lte=settings.TREE_DEPTH))
        # https://django-mptt.readthedocs.io/en/latest/mptt.utils.html#mptt.utils.get_cached_trees

        serializer = CommentSerializer(_comments, many=True,
                                       context={'max_depth': settings.TREE_DEPTH}, )
        return serializer.data

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ('comments', 'published_at', 'blog',)


class CommentSerializer(serializers.ModelSerializer):
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())
    parent = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False)
    children = serializers.SerializerMethodField('get_children')

    def get_children(self, comment):
        """ Получение всех комментариев к статье вплоть до 3 уровня вложенности. """
        max_depth = settings.TREE_DEPTH
        _children = comment.get_children()
        if (max_depth is not None) and (comment.get_level() >= max_depth):
            return []
        return CommentSerializer(_children, many=True, context={'max_depth': max_depth}).data

    class Meta:
        model = Comment
        exclude = ('lft', 'rght', 'tree_id')
        read_only_fields = ('lft', 'rght', 'tree_id', 'level', 'children')
