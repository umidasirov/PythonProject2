from django.urls import path
from .views import RegisterView, LoginView, ProfileView, UsersListView,ErtakView,FileViewSet

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.urls import path, include
router = DefaultRouter()
router.register(r'files', FileViewSet)
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('ertaklar/', ErtakView.as_view(), name='ertak'),
    path('api/', include(router.urls)),
]
# Загрузка файла (POST api/files/ с данными name, description, и полем file (multipart/form-data))
#
# Получение списка файлов (GET api/files/)
#
# Получение одного файла (GET api/files/{id}/)
#
# Скачивание файла (GET api/files/{id}/download/) — возвращает сам файл с заголовками для скачивания