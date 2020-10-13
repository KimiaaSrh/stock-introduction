from rest_framework import serializers
from.models import Post, Rating,JointoChat
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = '__all__'


class JointoChatSerializer(serializers.ModelSerializer):
  class Meta:
    model = JointoChat
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','username','password')
    extra_kwargs = {'password':{'write_only':True,'required':True}}

  def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      print(user)
      Token.objects.create(user=user)
      return user  