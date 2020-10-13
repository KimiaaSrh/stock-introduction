from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import PostViewSet,RatingViewSet, JointoChatViewSet,UserViewSet


router=routers.DefaultRouter()
router.register('post',PostViewSet)
router.register('rating',RatingViewSet)
router.register('joinchat',JointoChatViewSet)
router.register('users',UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]