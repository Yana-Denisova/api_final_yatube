from django.urls import path, include
from rest_framework import routers

from api.views import PostViewSet, GroupViewset, CommentViewset, FollowViewset

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewset)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewset, basename='comments')
router.register(r'follow', FollowViewset, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls), name='api'),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
