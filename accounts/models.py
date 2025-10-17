from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

import uuid


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise ValueError('Users must have a phone number.')

        email = kwargs.get('email')

        user = self.model(
            phone=phone,
            email=self.normalize_email(email) if email else None,
            fname=kwargs['fname'],
            lname=kwargs['lname'],
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        user = self.create_user(phone, password, **kwargs)
        user.is_admin = True
        user.client_type = 'emp'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(
        max_length=40,
        unique=True,
        blank=True,
        null=True
        )
    fname = models.CharField(
        max_length=50,
        verbose_name='first name'
    )
    lname = models.CharField(
        max_length=50,
        verbose_name='last name'
    )
    sex = models.CharField(
        max_length=30,
        choices=[
            ('m', 'Male'),
            ('f', 'Female'),
            ('o', 'Other')
        ],
        default='o',
    )
    birthday = models.DateField(blank=True, null=True)
    client_type = models.CharField(
        max_length=50,
        choices=[
            ('cli', 'Client'),
            ('emp', 'Employee'),
            ('pen', 'Pensioner'),
            ('nd', 'Not Defined'),
            ('sk', 'Schoolkid'),
            ('st', 'Student'),
        ],
        default='nd'
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['fname', 'lname',]

    @property
    def full_name(self):
        return f'{self.fname} {self.lname}'

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self) -> str:
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
