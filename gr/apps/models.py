#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomGroup(Group):
    field = models.TextField(blank=True)


class PersonManager(BaseUserManager):

    def create_user(self, email):
        password = Person.objects.make_random_password()
        person = self.model(email=email)
        return person

    def create_superuser(self, email, password):
        person = self.model(email=email,)
        person.set_password(password)
        person.is_admin = True
        person.save(using=self._db)
        return person


class Person(AbstractBaseUser):
    email = models.EmailField('email', unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(CustomGroup,
                                    verbose_name=_('customgroups'),
                                    blank=True,
                                    related_name="person_set",
                                    related_query_name="customuser",
                                    )
    USERNAME_FIELD = 'email'
    objects = PersonManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
