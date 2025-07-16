from .models import File
from rest_framework import serializers
from .models import User, Ertak, File
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import os


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'ism', 'familia', 'telRaqam', 'shaxar', 'tugulganKuni', 'avatar','courses')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'ism', 'familia', 'telRaqam', 'shaxar', 'tugulganKuni')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Правильное хэширование
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid email or password")

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }


class ErtakllarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ertak
        fields = ('name', 'img', 'description', 'stars', 'main_text', 'yosh', 'tip')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'description', 'file']


from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import FileResponse, Http404
import os

from .models import File
from .serializers import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'description', 'file', 'img']


from .models import Item, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'url']


class ItemSerializer(serializers.ModelSerializer):
    # Включаем сериализатор курсов для каждого элемента
    courses = CourseSerializer(many=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'img', 'courses']
