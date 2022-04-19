from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BlogViewSet, CommentViewSet, CreateBlog, CreateComment

router = SimpleRouter()
router.register('blogs', BlogViewSet, basename='blogs')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = router.urls

urlpatterns += [
    path('create_blog/', CreateBlog.as_view()),
    path('create_comment/', CreateComment.as_view()),
]
