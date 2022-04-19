from django.contrib.auth.models import User
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'id {self.id}: {self.title}'


class Comment(MPTTModel):
    """
    Comment model with hierarchy based on MPTT algorithm. Read more here:
    https://django-mptt.readthedocs.io/en/latest/overview.html#what-is-modified-preorder-tree-traversal
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    text = models.TextField(max_length=300)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'id {self.id}: {self.text}'
