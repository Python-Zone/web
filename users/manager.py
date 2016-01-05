# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, nickname, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not name:
            raise ValueError('Users must have an name')

        user = self.model(
            name=name,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, nickname, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(name,
            password=password,
            nickname=name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user