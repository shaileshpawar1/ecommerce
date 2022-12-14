from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=14,null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100,null=True,blank=True)
    forgot_password = models.CharField(max_length=100,null=True,blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    type = (
        (1,'Seller'),
        (2,'Customer')
    )
    user_type = models.IntegerField(choices=type,default=1)
    objects= UserManager()
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS= []