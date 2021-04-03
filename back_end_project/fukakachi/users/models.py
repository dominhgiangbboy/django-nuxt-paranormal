from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.
# users/models.py

class CustomAccountManager(BaseUserManager):
    def create_superuser(self,user_name,password, **other_fields):
        other_fields.setdefault('is_admin',True)
        return self.create_user(user_name,password, **other_fields)
    def create_user(self, user_name,password, **other_fields):
        user = self.model(user_name = user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
  

class NewUser(AbstractBaseUser,PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'user_name'
    # REQUIRED_FIELDS = ['password']

    def __str__(self) -> str:
        return self.user_name

