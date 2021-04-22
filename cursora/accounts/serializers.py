from .models import *
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from PIL import Image


class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")

    class Meta:
        model = Profile
        fields = ('username', 'id')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'email', 'is_staff', 'is_active']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "id", "last_login", "is_superuser", "email", "is_staff", "is_active", "date_joined", "user_permissions"]


class CommentarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Commentary
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):

#    commentary = CommentarySerializer(many=True)

    class Meta:
        model = Video
        read_only_fields = ('course', 'video_author', )
        fields = '__all__'


class VideoEasySerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ["title", "id", "preview", "date_pub"]

#   если комментарии мешают, впиши те поля, которые нужны^^^


class CourseSerializer(serializers.ModelSerializer):

    video = VideoEasySerializer(many=True, read_only=True, source='video_set')
    author = AuthorSerializer(read_only=True)

    class Meta:
        read_only_fields = ('date_pub', )
        model = Course
        fields = '__all__'


class CourseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        read_only_fields = ('author', 'date_pub')
        fields = '__all__'


class CourseEasySerializer(serializers.ModelSerializer):

    category_title = serializers.CharField(source="category.title")
    author = AuthorSerializer()

    class Meta:
        model = Course
        fields = ["title", "category_title", "description", "preview", "date_pub", "author", "id"]


class ProfileListSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    course = CourseEasySerializer(many=True, read_only=True, source='course_set')

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileEasySerializer(serializers.ModelSerializer):
    username = User.username

    class Meta:
        model = Profile
        fields = ["username"]


class ProfileUpdateSerializer(serializers.ModelSerializer):

    profile_pic = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Profile
        fields = ['profile_pic']


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    course = CourseEasySerializer(many=True, read_only=True, source='course_set')

    class Meta:
        model = Profile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
