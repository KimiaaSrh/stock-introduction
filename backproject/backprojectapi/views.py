from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Post, Rating,JointoChat
from .serializers import PostSerializer,RatingSerializer,JointoChatSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token


class PostViewSet(viewsets.ModelViewSet):
  queryset= Post.objects.all()
  serializer_class = PostSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  @action(methods=['POST'], detail=True)
  def create_post(self,request,pk=None):
    Writer = request.user.username
    extraField = request.data['extraField']
    name=request.data['name']
    description = request.data['description']
    postId=request.data['postId']
    postingDate = request.data['postingDate']
    postingTime=request.data['postingTime']
    companyField = request.data['companyField']
    avg1 = request.data['avg1']
    avg2 = request.data['avg2']
    avg3 = request.data['avg3']
    avg4 = request.data['avg4']
    avg5 = request.data['avg5']
    avg6 = request.data['avg6']
    avg7 = request.data['avg7']
    avg8 = request.data['avg8']
    avg9 = request.data['avg9']
    avg10 = request.data['avg10']
    avg11 = request.data['avg11']
    avg12 = request.data['avg12']
    std1 = request.data['std1']
    std2 = request.data['std2']
    std3 = request.data['std3']
    std4 = request.data['std4']
    std5 = request.data['std5']
    std6 = request.data['std6']
    std7 = request.data['std7']
    std8 = request.data['std8']
    std9 = request.data['std9']
    std10 = request.data['std10']
    std11 = request.data['std11']
    std12 = request.data['std12']
    rating =Post.objects.create(extraField=extraField,avg1=avg1,postId=postId,name=name,description=description,Writer=Writer,postingDate=postingDate,postingTime=postingTime,companyField=companyField,avg2=avg2,avg3=avg3,avg4=avg4,avg5=avg5,avg6=avg6,avg7=avg7,avg8=avg8,avg9=avg9,avg10=avg10,avg11=avg11,avg12=avg12,std1=std1,std2=std2,std3=std3,std4=std4,std5=std5,std6=std6,std7=std7,std8=std8,std9=std9,std10=std10,std11=std11,std12=std12)
    serializer = PostSerializer(rating,many=True)
    response = {'message':'rating created'}
    return Response(response, status=status.HTTP_200_OK)

class RatingViewSet(viewsets.ModelViewSet):
  queryset= Rating.objects.all()
  serializer_class = RatingSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  @action(methods=['POST'], detail=True)
  def create_rating(self,request,pk=None):
    stars = request.data['stars']
    ratingId = request.data['ratingId']
    comment = request.data['comment']
    ratingDate = request.data['ratingDate']
    ratingTime = request.data['ratingTime']
    extraField = request.data['extraField']
    rater=request.user
    postId = Post.objects.get(id=pk)
    rating =Rating.objects.create(postId=postId,extraField=extraField,ratingId=ratingId,rater=rater,stars=stars,comment=comment,ratingDate=ratingDate,ratingTime=ratingTime)
    serializer = RatingSerializer(rating,many=True)
    response = {'message':'rating created'}
    return Response(response, status=status.HTTP_200_OK)

class JointoChatViewSet(viewsets.ModelViewSet):
  queryset= JointoChat.objects.all()
  serializer_class = JointoChatSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  @action(methods=['POST'], detail=True)
  def create_joinToChat(self,request,pk=None):
    person = request.user
    extraField = request.data['extraField']
    textBody = request.data['textBody']
    dateOfSending = request.data['dateOfSending']
    timeOfSending = request.data['timeOfSending']
    rating =JointoChat.objects.create(extraField=extraField,person=person,textBody=textBody,dateOfSending=dateOfSending,timeOfSending=timeOfSending)
    serializer = JointoChatSerializer(rating,many=True)
    response = {'message':'rating created'}
    return Response(response, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = (AllowAny, )