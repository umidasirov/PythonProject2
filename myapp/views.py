from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Item

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, ErtakllarSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User, Ertak, File


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UsersListView(APIView):
    permission_classes = [IsAuthenticated]  # Kerak bo'lsa autentifikatsiya

    def get(self, request):
        users = User.objects.all()  # Barcha foydalanuvchilarni olish
        serializer = UserSerializer(users, many=True)  # Seriyalizatsiya qilish
        return Response(serializer.data)


class ErtakView(APIView):

    def get(self, request):
        ertaklar = Ertak.objects.all()
        serializer = ErtakllarSerializer(ertaklar, many=True)
        return Response(serializer.data)


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import FileResponse, Http404
from django.conf import settings
import os

from .models import File
from .serializers import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    # Кастомный метод для скачивания файла
    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        file_obj = self.get_object()
        file_path = file_obj.file.path

        if os.path.exists(file_path):
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
        else:
            raise Http404("Файл не найден")


from .serializers import ItemSerializer


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()  # Получаем все объекты Item
    serializer_class = ItemSerializer  # Используем сериализатор ItemSerializer
