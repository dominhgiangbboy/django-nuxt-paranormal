from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.
# users/models.py

class CustomAccountManager(BaseUserManager):
    def create_superuser(self,user_name,password, **other_fields):
        other_fields.setdefault('is_admin',True)
        return CustomAccountManager.create_user(self,user_name,password, **other_fields)
    
    def create_user(self, user_name, password, **other_fields):
        temp = NewUser.objects.filter(user_name = user_name)
        
        if len(temp) == 0 :
            user = NewUser.objects.create(user_name = user_name, **other_fields)
            user.set_password(password)
            user.save()
        else:
            user = None
        return user
  

class NewUser(AbstractBaseUser,PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=True)
    is_admin = models.BooleanField(default=False)
    is_dev = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    company = models.CharField(max_length=150, default ="")
    email = models.EmailField(default='example@email.com')
    objects = CustomAccountManager()
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['password']

    def __str__(self) -> str:
        return self.user_name

