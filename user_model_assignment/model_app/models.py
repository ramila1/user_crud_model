

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"),unique = True)
    phone = models.IntegerField(unique=True,null=True)
    address = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=10,choices=(('male','male'),('female','female'),('others','others')))
    age= models.IntegerField(null=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    
