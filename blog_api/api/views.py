from rest_framework import viewsets, generics, mixins
from .serializers import (
    PostSerializer,
    CommentSerializer,
    GetAllCommentarySerializer,
    PostWithCommentarySerializer,
)
from posts.models import Post, Comment


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        queryset = Comment.objects.filter(post=post_id)
        return queryset


class GetAllCommentaryList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = GetAllCommentarySerializer

    def get_queryset(self):
        comment_id = self.kwargs.get("comment_id")
        queryset = Comment.objects.filter(id=comment_id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetPostWithCommentaryList(
    mixins.ListModelMixin, generics.GenericAPIView
):
    queryset = Post.objects.all()
    serializer_class = PostWithCommentarySerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        queryset = Post.objects.filter(id=post_id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
