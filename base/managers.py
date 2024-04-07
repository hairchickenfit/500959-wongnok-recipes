from django.contrib.auth.models import BaseUserManager

from . import models as base_models


class WongnokUserManager(BaseUserManager):
    
    def create_user(
        self, first_name, last_name, email, password,
        is_active=True, is_superuser=False, is_staff=False
    ):
        if (not first_name) or (not last_name) or (not email) or (not password):
            raise ValueError('Something is missing.')
        wongnok_user_obj = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )
        wongnok_user_obj.set_password(password)
        wongnok_user_obj.is_active = is_active
        wongnok_user_obj.is_superuser = is_superuser
        wongnok_user_obj.is_staff = is_staff
        wongnok_user_obj.save(using=self._db)
        return wongnok_user_obj
    
    def create_superuser(
        self, first_name, last_name, email, password,
        is_active=True, is_superuser=True, is_staff=True
    ):  
        return self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password,
            is_active=is_active,
            is_superuser=is_superuser,
            is_staff=is_staff
        )      