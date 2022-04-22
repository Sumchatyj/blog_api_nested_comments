from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    CommentViewSet,
    GetAllCommentaryList,
    GetPostWithCommentaryList,
)

v1_router = DefaultRouter()
v1_router.register(r"posts", PostViewSet)
v1_router.register(r"posts/(?P<post_id>\d+)/comments", CommentViewSet)

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path("v1/comments/<int:comment_id>/", GetAllCommentaryList.as_view()),
    path(
        "v1/post-comments/<int:post_id>/", GetPostWithCommentaryList.as_view()
    ),
]
