from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from . import managers as base_managers


class WongnokUser(AbstractUser):
    
    # field(s) we do not want from AbstractUser, will be None
    username = None
    user_permissions = None
    groups = None
    # first_name, last_name, email, password, groups, user_permission,
    # is_staff, is_active, is_superuser, last_login, date_joined
    
    email = models.CharField(max_length=255, unique=True)
    
    # define
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = base_managers.WongnokUserManager()

    class Meta:
        verbose_name = 'wongnok user'
        verbose_name_plural = 'wongnok user(s)'
    
    def __str__(self) -> str:
        return self.email
    
    def get_absolute_url(self):
        return reverse(
            'wongnok_user_email',
            kwargs={'pk': self.email}
        )