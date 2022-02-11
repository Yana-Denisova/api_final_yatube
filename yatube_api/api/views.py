from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Group, Post, Follow
from .permissions import AuthorOrReadOnly, OwnerOrReadOnly
from .serializers import (CommentSerializer,
                          GroupSerializer, PostSerializer, FollowSerializer)


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [OwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewset(viewsets.ModelViewSet):
    permission_classes = [OwnerOrReadOnly]
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        get_object_or_404(Post, id=post_id)
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        current_post = get_object_or_404(Post, id=post_id)
        serializer.save(post=current_post, author=self.request.user)


class FollowViewset(viewsets.ModelViewSet):
    permission_classes = [AuthorOrReadOnly]
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^following__username',)

    def get_queryset(self):
        new_queryset = Follow.objects.prefetch_related('user__follower').filter(user=self.request.user)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
