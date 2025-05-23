from django.urls import path
from .views import RegisterView, LoginView, ProfileView, UsersListView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', UsersListView.as_view(), name='users-list'),
]
