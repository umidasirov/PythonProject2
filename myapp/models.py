# models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email bo'lishi kerak")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    familia = models.CharField(max_length=100)
    ism = models.CharField(max_length=100)
    telRaqam = models.CharField(max_length=15)
    tugulganKuni = models.CharField(max_length=100)
    shaxar = models.CharField(max_length=200)
    avatar = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['ism', 'familia']

    def __str__(self):
        return f"{self.ism} {self.familia}"


class Xulosa(models.Model):
    ertak = models.ForeignKey('Ertak', on_delete=models.CASCADE, related_name='xulosalar')
    xulosa = models.TextField()

    def __str__(self):
        return self.xulosa[:50] + '...'


class Ertak(models.Model):
    name = models.CharField(max_length=255)
    is_favour = models.BooleanField(default=False)
    img = models.URLField()
    description = models.TextField()
    stars = models.CharField(max_length=10)
    main_text = models.TextField()
    yosh = models.CharField(max_length=100, blank=True)  # yoki IntegerField, agar yosh raqam bo'lsa
    tip = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/')  # файлы будут сохраняться в media/uploads/
    img = models.URLField()

    def __str__(self):
        return self.name
