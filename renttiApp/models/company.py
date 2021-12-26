from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        """
        Creates and saves a user_company with the given company and password.
        """
        if not username:
            raise ValueError('Companies must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser_company with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Company(AbstractBaseUser, PermissionsMixin):
    #primary key
    id = models.BigAutoField(primary_key=True)
    nit_rut = models.IntegerField('nit_rut')
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    name = models.CharField('Name', max_length = 30)
    office_address = models.CharField('office_address',max_length=50)
    telephone_number = models.IntegerField('telephone_number')
    corporate_email = models.EmailField('corporate_email',max_length=50)
    web_site = models.CharField('web_site',max_length=50)
    chamber_of_comerce = models.CharField('chamber_of_comerce', max_length=30)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'