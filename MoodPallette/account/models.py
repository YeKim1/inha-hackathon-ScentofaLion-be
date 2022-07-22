from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, password):
        user = self.model(
            email = email,
            nickname = nickname,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email = email,
            nickname = nickname,
            password = password
        )
        user.is_admin = True
        user.save(using=self.db)
        return user



class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def is_staff(self):
        return self.is_admin
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    